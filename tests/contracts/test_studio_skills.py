"""Studio skill layout for this fork stays discoverable and lightweight."""

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
AGENTS = REPO / ".agents" / "skills"
CLAUDE = REPO / ".claude" / "skills"

REMOTION_SKILLS = [
    "remotion-best-practices",
    "remotion-captions",
    "remotion-create",
    "remotion-docs",
    "remotion-interactivity",
    "remotion-license",
    "remotion-maps",
    "remotion-markup",
    "remotion-multimedia",
    "remotion-render",
    "remotion-saas",
    "remotion-studio",
    "remotion-upgrade",
]

HYPERFRAMES_SKILLS = [
    "hyperframes",
    "hyperframes-cli",
    "hyperframes-registry",
    "media-use",
    "remotion-to-hyperframes",
    "figma",
    "reverse-any-video",
    "slideshow",
    "style-sampling",
]

MEDIA_SUFFIXES = {
    ".ogg",
    ".wav",
    ".mp3",
    ".flac",
    ".m4a",
    ".mp4",
    ".webm",
    ".mov",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
}


def test_thirteen_remotion_skills_and_preserved_rules():
    assert len(REMOTION_SKILLS) == 13
    for name in REMOTION_SKILLS:
        skill = AGENTS / name / "SKILL.md"
        assert skill.is_file(), skill
        link = CLAUDE / name
        assert link.is_symlink(), f"{link} should be a symlink, not a second copy"
        assert link.resolve() == skill.parent.resolve()
    rules = AGENTS / "remotion-best-practices" / "rules"
    assert (rules / "animations.md").is_file()
    assert (rules / "sfx.md").is_file()
    assert (rules / "charts.md").is_file()
    router = (AGENTS / "remotion-best-practices" / "SKILL.md").read_text(encoding="utf-8")
    assert "../remotion-markup/SKILL.md" in router
    assert "rules/animations.md" in router
    assert not (AGENTS / "remotion-best-practices" / "remotion-markup").exists()


def test_hyperframes_skills_travel_with_the_repo():
    for name in HYPERFRAMES_SKILLS:
        skill = AGENTS / name / "SKILL.md"
        assert skill.is_file(), skill
        link = CLAUDE / name
        assert link.is_symlink()
        assert link.resolve() == skill.parent.resolve()
    # The 0.7 split skills stay, because stage directors still name them.
    assert (AGENTS / "hyperframes-core" / "SKILL.md").is_file()
    provenance = (AGENTS / "hyperframes" / "PROVENANCE.md").read_text(encoding="utf-8")
    assert "4067efc" in provenance


def test_motion_house_rules_are_wired():
    skill = AGENTS / "motion-cinco-efectos" / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    assert "name: motion-cinco-efectos" in text
    assert "Mask reveals" in text
    guide = (REPO / "AGENT_GUIDE.md").read_text(encoding="utf-8")
    agents = (REPO / "AGENTS.md").read_text(encoding="utf-8")
    assert "motion-cinco-efectos" in guide
    assert "motion-cinco-efectos" in agents
    scene = (REPO / "skills" / "pipelines" / "explainer" / "scene-director.md").read_text(
        encoding="utf-8"
    )
    assert "motion-cinco-efectos" in scene


def test_stickman_skill_has_no_committed_media():
    root = AGENTS / "directing-stickman-videos"
    assert (root / "SKILL.md").is_file()
    assert (root / "ASSETS.md").is_file()
    assert (REPO / "scripts" / "install-stickman-assets.sh").is_file()
    library = root / "assets"
    media = [
        path
        for path in library.rglob("*")
        if path.is_file() and path.suffix.lower() in MEDIA_SUFFIXES
    ]
    for path in media:
        ignored = subprocess.run(
            ["git", "check-ignore", "-q", "--", str(path)],
            cwd=REPO,
            check=False,
        )
        assert ignored.returncode == 0, f"stickman media would be committed: {path}"
    link = CLAUDE / "directing-stickman-videos"
    assert link.is_symlink()
    assert link.resolve() == root.resolve()


def test_estudio_documents_spanish_local_helpers():
    doc = (REPO / "ESTUDIO.md").read_text(encoding="utf-8")
    assert "model" in doc and "small" in doc
    assert "small.en" in doc
    assert "es_MX-ald-medium" in doc
    assert "es_ES-davefx-medium" in doc
    assert "earshot" in doc
    assert "uv tool install" in doc
    assert "npx hyperframes doctor" in doc
    assert "hasta 3 personas" in doc
    # The beginner doc must not ship credentials.
    lowered = doc.lower()
    assert "api_key=" not in lowered
    assert "sk-" not in lowered
