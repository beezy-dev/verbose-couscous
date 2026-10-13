# beezy.dev

Official repository for [beezy.dev](https://beezy.dev) — Technical Stewardship & Deep Systems Engineering advisory in **AI Data Foundations**, **Zero-Trust Cryptography**, **Cloud-Native Storage**, and **AI Software Factory Orchestration (AIMES)**.

## Architecture

- **Format**: Zero-dependency, high-performance static web application (`index.html` + Vanilla CSS).
- **Hosting**: GitHub Pages via automated GitHub Actions pipeline.
- **Custom Domain**: `beezy.dev` (configured via `CNAME`).

## Local Development

Preview the website locally using any standard HTTP server:

```bash
# Python 3
python3 -m http.server 8000

# Open in browser
open http://localhost:8000
```

## Deployment

Pushes to the `main` branch trigger `.github/workflows/publish.yml`, which deploys the static assets directly to the `gh-pages` branch using GitHub's native `GITHUB_TOKEN`. No external tokens, python dependencies, or build containers required.

## Archives

- `_archive_mkdocs/`: Historical documentation and MkDocs notes preserved for reference.
- `_design_previews/`: Alternative design explorations (The Systems Kernel, The Hive Sovereign, The Runtime Console).

## License

[Apache-2.0](LICENSE)
