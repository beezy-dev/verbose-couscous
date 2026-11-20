# beezy.dev

Official repository for [beezy.dev](https://beezy.dev) — an **Open Systems Research & Engineering Hub** maintained by Rom Adams (`romdalf`) covering **Data Foundations for Agentic Access**, **Zero-Trust Cryptography Architecture** (**Kleidi**), **AI Manufacturing Execution Systems** (**AIMES**), and **Agentic Source Control & Cognitive Lineage Data Planes** (**ENNOIA**).

## Architecture

- **Format**: Zero-dependency, high-performance static web application (`index.html` + Vanilla CSS/JS, styled in a Charmbracelet Lip Gloss CLI TUI aesthetic).
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

## Archives & Previews

- `_archive_mkdocs/`: Historical documentation and MkDocs notes preserved for reference.
- `_design_previews/`: Design preview options (`option1-lipgloss-cli.html` Lip Gloss CLI, `option2-ascii-blue.html` CRT Blue ASCII, `option3-ascii-hub.html` CRT Amber ASCII).

## License

[Apache-2.0](LICENSE)
