#!/usr/bin/env python3
"""
Unit and integration verification tests for beezy.dev website structure and content.
"""
from html.parser import HTMLParser
import os
import re
import unittest
from pathlib import Path

SITE_DIR = Path(__file__).parent.resolve()


class _DocumentStructureParser(HTMLParser):
    """Lightweight HTML parser to validate landmarks, titles, and heading hierarchy."""

    def __init__(self):
        super().__init__()
        self.html_lang = None
        self.in_title = False
        self.title_text = []
        self.h1_count = 0
        self.main_count = 0
        self.heading_levels = []
        self.iframe_titles = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        if tag == "html":
            self.html_lang = attr_map.get("lang")
        elif tag == "title":
            self.in_title = True
        elif tag == "main":
            self.main_count += 1
        elif tag == "iframe":
            self.iframe_titles.append(attr_map.get("title", ""))
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1])
            self.heading_levels.append(level)
            if level == 1:
                self.h1_count += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)


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
        """Verify live index.html contains promoted Lip Gloss CLI research hub content, metadata, and manual edits."""
        index_path = SITE_DIR / "index.html"
        html = index_path.read_text(encoding="utf-8")
        html_norm = re.sub(r"\s+", " ", html)
        html_lower = html_norm.lower()

        # Title, Open Graph metadata, and Branding
        self.assertIn("beezy.dev", html_norm)
        self.assertIn("Open Systems Research &amp; Engineering", html_norm)
        self.assertIn('property="og:url" content="https://beezy.dev/"', html_norm)
        self.assertIn('property="og:title"', html_norm)
        self.assertIn('name="twitter:card"', html_norm)

        # Disallowed legacy enterprise sales copy & outdated location
        for forbidden in [
            "Initiate Technical Briefing",
            "1–2 Days Per Week",
            "Fixed Sprint",
            "Request Audit",
            "Scope Project",
            "1 SLOT AVAILABLE",
            "OpenShift",
            "Technical Stewardship & Deep Systems Engineering",
        ]:
            self.assertNotIn(forbidden, html_norm)
        self.assertNotIn("brussels", html_lower)

        # Projects & 4 Research Domains
        self.assertIn("01 // Projects", html_norm)
        self.assertNotIn("01 // Active Projects", html_norm)

        project_tab_ids = ["tab-aimes", "tab-ennoia", "tab-kleidi", "tab-trousseau", "tab-discoblocks"]
        positions = [html.index(f'id="{tid}"') for tid in project_tab_ids]
        self.assertEqual(positions, sorted(positions), "Project tabs are not in the required order")
        self.assertIn('id="tab-aimes" class="lip-tab" aria-selected="true"', html_norm)

        for badge_cls in [
            "lip-badge--active",
            "lip-badge--rd",
            "lip-badge--paused",
            "lip-badge--deprecated",
        ]:
            self.assertIn(badge_cls, html_norm, f"index.html missing status badge class: {badge_cls}")

        for term in [
            "Rom Adams",
            "Netherlands",
            "StorageOS/Ondat",
            "max-inline-size: 110ch",
            "Kleidi",
            "KMSv2",
            "https://github.com/beezy-dev/kleidi",
            "AIMES",
            "ENNOIA",
            "Discoblocks",
            "https://github.com/ondat/discoblocks",
            "https://github.com/ondat/trousseau",
            "2024&ndash;2026",
            "2020&ndash;2024",
            "2021&ndash;2024",
            "R&amp;D",
            "Paused",
            "Deprecated",
            "cognitive lineage",
            "data plane",
            "Data Foundations for Agentic Access",
            "Zero-Trust Cryptography Architecture",
            "AI Manufacturing Execution System",
            "Data Plane with Cognitive Lineage",
            "Kubernetes Secrets Handbook",
            "The Kubernetes Bible",
            "Kubernetes – An Enterprise Guide",
            "Trousseau",
            "CSI",
            "Zero-trust architecture for secret handling",
            "Virtual file system projection",
            "Identity validation in agentic workflow",
        ]:
            self.assertIn(term, html_norm, f"index.html missing required term: {term}")

        self.assertIn("fractional engineering", html_lower)

        # Lip Gloss TUI design + user's manual edits (3-step staircase, no swatch grid, no email in #about)
        for lip_token in [
            "term-window",
            "lip-stair",
            "stair-1",
            "stair-2",
            "stair-3",
            "lip-dialog",
            "lip-purple-card",
            "lip-statusbar",
            "UTF-8",
            "&#10003;",
            "#171717",
            "#874bfd",
            "#6b46e5",
            "#d62e6e",
            "#43bf6d",
        ]:
            self.assertIn(lip_token, html_norm)

        self.assertNotIn("stair-4", html_norm)
        self.assertNotIn("stair-5", html_norm)
        self.assertNotIn("lip-swatch-grid", html_norm)

        about_match = re.search(r'<section id="about"[^>]*>(.*?)</section>', html, re.S)
        self.assertIsNotNone(about_match, "index.html missing #about section")
        about_html = about_match.group(1)
        self.assertNotIn("rom@beezy.dev", about_html)
        self.assertNotIn("mailto:", about_html)
        self.assertIn("https://github.com/beezy-dev", about_html)
        self.assertIn("https://www.linkedin.com/in/romdalf/", about_html)

    def test_ada_and_accessibility_features(self):
        """Verify ADA / WCAG 2.1 & 2.2 AA accessibility and modern web features in live index.html."""
        index_path = SITE_DIR / "index.html"
        html = index_path.read_text(encoding="utf-8")

        parser = _DocumentStructureParser()
        parser.feed(html)
        self.assertEqual(parser.html_lang, "en")
        self.assertTrue("".join(parser.title_text).strip())
        self.assertEqual(parser.h1_count, 1)
        self.assertEqual(parser.main_count, 1)
        for idx in range(1, len(parser.heading_levels)):
            self.assertLessEqual(parser.heading_levels[idx], parser.heading_levels[idx - 1] + 1)

        for token in [
            'class="skip-link"',
            "Skip to main content",
            'id="main-content"',
            ":focus-visible",
            "@media (prefers-reduced-motion: reduce)",
            "@media (forced-colors: active)",
            "color-scheme: dark",
            "aria-label=",
            'aria-hidden="true"',
            'aria-live="polite"',
            "aria-pressed=",
            "A11Y: WCAG-AA",
            'data-tabs="projects"',
            'data-tabs="research"',
            'hidden="until-found"',
            "beforematch",
        ]:
            self.assertIn(token, html)

        self.assertEqual(len(re.findall(r'<div[^>]*role="tablist"', html)), 2)
        self.assertEqual(html.count('<button type="button" role="tab"'), 9)
        self.assertEqual(len(re.findall(r'<div[^>]*role="tabpanel"', html)), 9)
        self.assertNotIn("aria-controls=", html)
        self.assertNotIn("onclick=", html)
        self.assertNotIn("onsubmit=", html)
        self.assertNotIn("clip: rect(", html)
        self.assertNotIn("animation-duration: 0.01ms", html)
        self.assertIsNone(re.search(r"font-size\s*:\s*[^;]*\dpx", html))

    def test_asset_references(self):
        """Verify that local relative image references in index.html actually exist."""
        index_path = SITE_DIR / "index.html"
        html = index_path.read_text(encoding="utf-8")

        src_matches = re.findall(r'(?:src|href)=["\'](images/[^"\']+)["\']', html)
        for rel_path in src_matches:
            full_path = SITE_DIR / rel_path
            self.assertTrue(full_path.exists(), f"Referenced asset not found: {rel_path}")

    def test_github_workflow_structure(self):
        """Verify publish.yml deploys to gh-pages branch without external secrets."""
        workflow_path = SITE_DIR / ".github" / "workflows" / "publish.yml"
        content = workflow_path.read_text(encoding="utf-8")
        self.assertIn("gh-pages", content)
        self.assertIn("git push origin HEAD:gh-pages --force", content)
        self.assertNotIn("INSIDERS", content)
        self.assertNotIn("peaceiris", content)

class TestDesignPreviews(unittest.TestCase):
    PREVIEWS_DIR = SITE_DIR / "_design_previews"
    OPTION_FILES = [
        "option1-lipgloss-cli.html",
        "option2-ascii-blue.html",
        "option3-ascii-hub.html",
    ]
    LEGACY_FILES = [
        "option1-systems-kernel.html",
        "option2-hive-sovereign.html",
        "option3-runtime-console.html",
        "option1-research-hub.html",
        "option2-lab-notebook.html",
        "option1-ascii-purple.html",
    ]

    def test_preview_files_and_cleanup(self):
        """Verify Lip Gloss CLI, CRT Blue, and CRT Amber preview options exist and legacy previews are removed."""
        switcher = self.PREVIEWS_DIR / "index.html"
        self.assertTrue(switcher.exists(), "Missing _design_previews/index.html")
        self.assertGreater(switcher.stat().st_size, 0)

        for name in self.OPTION_FILES:
            path = self.PREVIEWS_DIR / name
            self.assertTrue(path.exists(), f"Missing preview file: {name}")
            self.assertGreater(path.stat().st_size, 0, f"Empty preview file: {name}")

        for old_name in self.LEGACY_FILES:
            old_path = self.PREVIEWS_DIR / old_name
            self.assertFalse(old_path.exists(), f"Superseded file still exists: {old_name}")

    def test_switcher_hub_integrity(self):
        """Verify _design_previews/index.html wires Lip Gloss CLI (default), CRT Blue, and CRT Amber options."""
        html = (self.PREVIEWS_DIR / "index.html").read_text(encoding="utf-8")
        for name in self.OPTION_FILES:
            self.assertIn(name, html)

        self.assertIn('src="option1-lipgloss-cli.html"', html)
        for badge in ["Charm TUI", "CRT Blue", "CRT Amber"]:
            self.assertIn(badge, html)

        parser = _DocumentStructureParser()
        parser.feed(html)
        self.assertEqual(parser.html_lang, "en")
        self.assertTrue("".join(parser.title_text).strip())
        self.assertTrue(any(t.strip() for t in parser.iframe_titles), "iframe must have a non-empty title")
        self.assertNotIn("onclick=", html)
        self.assertNotIn('scrolling="no"', html)
        self.assertNotIn("clip: rect(", html)
        self.assertIsNone(re.search(r"font-size\s*:\s*[^;]*\dpx", html))

    def test_options_research_content_and_modern_web_hygiene(self):
        """Verify all 3 CRT ASCII options preserve manual edits, content, distinct palettes, and a11y/CSS rules."""
        required_terms = [
            "beezy.dev",
            "Open Systems Research &amp; Engineering",
            "Rom Adams",
            "StorageOS/Ondat",
            "max-inline-size: 110ch",
            "Netherlands",
            "rom@beezy.dev",
            "https://github.com/beezy-dev/kleidi",
            "https://github.com/beezy-dev",
            "https://www.linkedin.com/in/romdalf/",
            "Kleidi",
            "KMSv2",
            "AIMES",
            "ENNOIA",
            "cognitive lineage",
            "data plane",
            "Data Foundations for Agentic Access",
            "Zero-Trust Cryptography Architecture",
            "AI Manufacturing Execution System",
            "Data Plane with Cognitive Lineage",
            "Kubernetes Secrets Handbook",
            "The Kubernetes Bible",
            "Kubernetes – An Enterprise Guide",
            "Trousseau",
            "CSI",
            "Zero-trust architecture for secret handling",
            "Virtual file system projection",
            "Identity validation in agentic workflow",
        ]

        disallowed_sales_copy = [
            "Initiate Technical Briefing",
            "1–2 Days Per Week",
            "Fixed Sprint",
            "Request Audit",
            "Scope Project",
            "OpenShift",
            "1 SLOT AVAILABLE",
        ]

        palette_expectations = {
            "option1-lipgloss-cli.html": (["#171717", "#874bfd", "#6b46e5", "#d62e6e", "#43bf6d"], ["#ffb000"]),
            "option2-ascii-blue.html": (["#01060d", "#38bdf8", "#e0f2fe"], ["#ffb000"]),
            "option3-ascii-hub.html": (["#070500", "#ffb000", "#ffe3a3"], []),
        }

        for name in self.OPTION_FILES:
            with self.subTest(preview=name):
                html = (self.PREVIEWS_DIR / name).read_text(encoding="utf-8")
                html_norm = re.sub(r"\s+", " ", html)
                html_lower = html_norm.lower()

                for term in required_terms:
                    self.assertIn(term, html_norm, f"{name} missing required term: {term}")

                self.assertIn("fractional engineering", html_lower, f"{name} missing fractional engineering reference")
                self.assertNotIn("brussels", html_lower, f"{name} should use Netherlands instead of Brussels")

                for forbidden in disallowed_sales_copy:
                    self.assertNotIn(forbidden, html, f"{name} contains forbidden sales copy: {forbidden}")

                expected_colors, excluded_colors = palette_expectations[name]
                for col in expected_colors:
                    self.assertIn(col, html_lower, f"{name} missing expected palette color: {col}")
                for col in excluded_colors:
                    self.assertNotIn(col, html_lower, f"{name} contains unexpected color token: {col}")

                # HTML structural checks
                parser = _DocumentStructureParser()
                parser.feed(html)
                self.assertEqual(parser.html_lang, "en")
                self.assertTrue("".join(parser.title_text).strip())
                self.assertEqual(parser.h1_count, 1, f"{name} must have exactly one <h1>")
                self.assertEqual(parser.main_count, 1, f"{name} must have exactly one <main>")
                for idx in range(1, len(parser.heading_levels)):
                    self.assertLessEqual(
                        parser.heading_levels[idx],
                        parser.heading_levels[idx - 1] + 1,
                        f"{name} skipped heading level: {parser.heading_levels}",
                    )

                # Accessibility & modern web compliance
                for token in [
                    'class="skip-link"',
                    'id="main-content"',
                    ":focus-visible",
                    "@media (prefers-reduced-motion: reduce)",
                    "@media (forced-colors: active)",
                    "color-scheme: dark",
                    'aria-live="polite"',
                    "aria-pressed=",
                    "A11Y: WCAG-AA",
                ]:
                    self.assertIn(token, html, f"{name} missing required a11y/CSS token: {token}")

                self.assertNotIn("onclick=", html)
                self.assertNotIn("onsubmit=", html)
                self.assertNotIn("clip: rect(", html)
                self.assertNotIn("animation-duration: 0.01ms", html)
                self.assertIsNone(
                    re.search(r"font-size\s*:\s*[^;]*\dpx", html),
                    f"{name} uses forbidden px unit in font-size",
                )

                # Relative image assets resolve cleanly from _design_previews/
                asset_matches = re.findall(r'(?:src|href)=["\'](\.\./images/[^"\']+)["\']', html)
                self.assertTrue(asset_matches, f"{name} should reference ../images/ favicon")
                for rel_path in asset_matches:
                    resolved = (self.PREVIEWS_DIR / rel_path).resolve()
                    self.assertTrue(resolved.exists(), f"{name} references missing asset: {rel_path}")

    def test_ascii_hub_specifics(self):
        """Verify all 3 CLI/ASCII previews share streamlined layout, tabbed projects/research, and no About email."""
        for name in self.OPTION_FILES:
            with self.subTest(preview=name):
                html = (self.PREVIEWS_DIR / name).read_text(encoding="utf-8")
                html_norm = re.sub(r"\s+", " ", html)
                if name == "option1-lipgloss-cli.html":
                    for lip_token in [
                        "01 // Projects",
                        "term-window",
                        "lip-stair",
                        "lip-dialog",
                        "lip-purple-card",
                        "lip-statusbar",
                        "lip-badge--active",
                        "lip-badge--rd",
                        "lip-badge--paused",
                        "lip-badge--deprecated",
                        "Discoblocks",
                        "2024&ndash;2026",
                        "2020&ndash;2024",
                        "2021&ndash;2024",
                        "UTF-8",
                        "&#10003;",
                    ]:
                        self.assertIn(lip_token, html_norm, f"{name} missing Lip Gloss TUI token: {lip_token}")
                    self.assertNotIn("01 // Active Projects", html_norm)
                    self.assertNotIn("lip-swatch-grid", html, f"{name} should preserve removal of lip-swatch-grid")
                    project_tab_ids = ["tab-aimes", "tab-ennoia", "tab-kleidi", "tab-trousseau", "tab-discoblocks"]
                    positions = [html.index(f'id="{tid}"') for tid in project_tab_ids]
                    self.assertEqual(positions, sorted(positions), f"{name} project tabs out of order")
                    expected_tab_count = 9
                else:
                    for glyph in ["┌", "└", "│", "├──", "└──"]:
                        self.assertIn(glyph, html, f"{name} missing ASCII/box-drawing glyph: {glyph}")
                    expected_tab_count = 7
                for removed_block in [
                    "STACK_TOPOLOGY",
                    "HOST:",
                    "Interactive Research Shell",
                    'id="shell"',
                    "[04:SHELL]",
                    "ascii-art",
                    "ascii-actions",
                    '<figure class="ascii-table-figure"',
                ]:
                    self.assertNotIn(removed_block, html, f"{name} should not contain removed block: {removed_block}")

                self.assertIn("font-family: var(--font-mono);", html)

                # Tabbed Projects & Research widgets
                for tab_group in ['data-tabs="projects"', 'data-tabs="research"']:
                    self.assertIn(tab_group, html)
                self.assertEqual(len(re.findall(r'<div[^>]*role="tablist"', html)), 2)
                self.assertEqual(html.count('<button type="button" role="tab"'), expected_tab_count)
                self.assertEqual(len(re.findall(r'<div[^>]*role="tabpanel"', html)), expected_tab_count)
                self.assertIn('hidden="until-found"', html)
                self.assertIn("beforematch", html)
                self.assertNotIn("aria-controls=", html)

                # About section must omit email while retaining GitHub and LinkedIn
                about_match = re.search(r'<section id="about"[^>]*>(.*?)</section>', html, re.S)
                self.assertIsNotNone(about_match, f"{name} missing #about section")
                about_html = about_match.group(1)
                self.assertNotIn("rom@beezy.dev", about_html)
                self.assertNotIn("mailto:", about_html)
                self.assertIn("https://github.com/beezy-dev", about_html)
                self.assertIn("https://www.linkedin.com/in/romdalf/", about_html)


if __name__ == "__main__":
    unittest.main()
