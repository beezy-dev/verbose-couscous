#!/usr/bin/env python3
"""
Unit and integration verification tests for beezy.dev website structure and content.
"""
import os
import re
import unittest
from pathlib import Path

SITE_DIR = Path(__file__).parent.resolve()

class TestBeezyDevWebsite(unittest.TestCase):
    def test_core_files_exist(self):
        """Verify essential files for GitHub Pages static deployment exist."""
        required_files = [
            SITE_DIR / "index.html",
            SITE_DIR / "CNAME",
            SITE_DIR / ".nojekyll",
            SITE_DIR / "LICENSE",
            SITE_DIR / "README.md",
            SITE_DIR / ".github" / "workflows" / "publish.yml",
        ]
        for f in required_files:
            self.assertTrue(f.exists(), f"Missing required file: {f}")

    def test_cname_content(self):
        """Verify CNAME file points to beezy.dev."""
        cname_path = SITE_DIR / "CNAME"
        content = cname_path.read_text().strip()
        self.assertEqual(content, "beezy.dev")

    def test_favicon_exists(self):
        """Verify favicon image exists and is non-empty."""
        favicon = SITE_DIR / "images" / "favicon.png"
        self.assertTrue(favicon.exists(), "favicon.png does not exist")
        self.assertGreater(favicon.stat().st_size, 0, "favicon.png is empty")

    def test_index_html_content(self):
        """Verify index.html contains all critical sections and metadata."""
        index_path = SITE_DIR / "index.html"
        html = index_path.read_text(encoding="utf-8")

        # Title and Branding
        self.assertIn("beezy.dev", html)
        self.assertIn("Technical Stewardship & Deep Systems Engineering", html)

        # 4 Core Specifications
        self.assertIn("SPEC-01", html)
        self.assertIn("AI Data Foundations & Pipeline Architecture", html)
        self.assertIn("SPEC-02", html)
        self.assertIn("Zero-Trust Cryptography & Secrets Architecture", html)
        self.assertNotIn("Zero-Trust Cryptography (KMS)", html)  # Ensure (KMS) was removed
        self.assertIn("SPEC-03", html)
        self.assertIn("Enterprise Platform Scale & Storage (CSI)", html)
        self.assertIn("SPEC-04", html)
        self.assertIn("AIMES: AI Manufacturing Execution System", html)

        # Verified Artifacts (No Emojis, Bracketed Tags)
        self.assertIn("[PUB]", html)
        self.assertIn("Kubernetes Secrets Handbook", html)
        self.assertIn("[OSS]", html)
        self.assertIn("Kleidi", html)
        self.assertIn("Trousseau", html)
        self.assertIn("[SYS]", html)
        self.assertIn("Flagship: AIMES Orchestration", html)

        # 3 Patents Pending
        self.assertIn("[PAT]", html)
        self.assertIn("Intellectual Property: Patents Pending", html)
        self.assertIn("Zero-trust architecture for secret handling", html)
        self.assertIn("Virtual file system projection", html)
        self.assertIn("Identity validation in agentic workflow", html)

    def test_asset_references(self):
        """Verify that local relative image references in index.html actually exist."""
        index_path = SITE_DIR / "index.html"
        html = index_path.read_text(encoding="utf-8")

        src_matches = re.findall(r'(?:src|href)=["\'](images/[^"\']+)["\']', html)
        for rel_path in src_matches:
            full_path = SITE_DIR / rel_path
            self.assertTrue(full_path.exists(), f"Referenced asset not found: {rel_path}")

    def test_github_workflow_structure(self):
        """Verify publish.yml uses GitHub Pages deploy pattern with GITHUB_TOKEN."""
        workflow_path = SITE_DIR / ".github" / "workflows" / "publish.yml"
        content = workflow_path.read_text(encoding="utf-8")
        self.assertIn("peaceiris/actions-gh-pages@v4", content)
        self.assertIn("secrets.GITHUB_TOKEN", content)
        self.assertIn("cname: beezy.dev", content)
        self.assertNotIn("INSIDERS", content)  # Private token eliminated

if __name__ == "__main__":
    unittest.main()
