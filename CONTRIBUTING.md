# Contributing to Awesome Isaac

Thank you for your interest in contributing to this curated collection of NVIDIA Isaac ecosystem resources! This repository aims to be a comprehensive, high-quality resource for the robotics and reinforcement learning community. Whether you want to suggest a new paper, fix a broken link, or improve our documentation, your contributions are welcome.

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Resource Submission Guidelines](#resource-submission-guidelines)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)
- [How the Research Bot Works](#how-the-research-bot-works)
- [Code of Conduct](#code-of-conduct)
- [Questions and Contact](#questions-and-contact)

---

## Ways to Contribute

### Suggesting Resources

Help grow this collection by suggesting:

- **Research Papers**: Academic papers related to Isaac Gym, Isaac Lab, or Isaac Sim
- **Tools and Libraries**: RL frameworks, utilities, or extensions that work with Isaac Gym
- **Tutorials and Guides**: Educational content, video tutorials, or blog posts
- **Community Projects**: Open-source implementations, example environments, or applications

### Fixing Broken Links

Links can become outdated over time. If you find a broken link:

1. Open an issue describing which link is broken and where it is located
2. If possible, suggest an updated URL or an alternative resource
3. Or submit a pull request with the fix directly

### Improving Documentation

Help make this repository more accessible by:

- Clarifying descriptions of existing resources
- Adding missing information to resource entries
- Improving organization and categorization
- Fixing typos or grammatical errors
- Translating content (coordinate with maintainers first)

### Reporting Issues

Found a problem? Please open an issue with:

- A clear, descriptive title
- The location of the issue (section, line number, or URL)
- A description of what is wrong
- Suggestions for how to fix it (if applicable)

---

## Resource Submission Guidelines

### Required Information

Every resource submission must include:

| Field | Description | Required |
|-------|-------------|----------|
| **Title** | Clear, descriptive name of the resource | Yes |
| **URL** | Direct link to the resource | Yes |
| **Description** | Brief explanation of what it is/does (1-2 sentences) | Yes |
| **Category** | Which section it belongs in | Yes |
| **Year/Date** | Publication or release date | Recommended |
| **Authors** | Creator(s) of the resource | For papers |

### Quality Criteria

Resources should meet the following standards:

- **Relevance**: Directly related to NVIDIA Isaac Gym, Isaac Lab, or Isaac Sim
- **Maintained**: Actively maintained or still functional (for tools/code)
- **Documented**: Has sufficient documentation for users to get started
- **Accessible**: Publicly available (open access preferred for papers)
- **Quality**: Provides value to the robotics/RL community

### Format Examples

#### Research Papers

```markdown
- **[Paper Title](https://project-page-url):** Brief description of the contribution (Conference/Journal Year)
  - [Paper](https://arxiv.org/abs/XXXX.XXXXX)
  - [Code](https://github.com/user/repo)
  - Key feature or finding 1
  - Key feature or finding 2
```

**Example:**
```markdown
- **[Factory: Fast Contact for Robotic Assembly](https://sites.google.com/nvidia.com/factory):** High-fidelity contact simulation for robotic assembly tasks (RSS 2022)
  - [Paper](http://doi.acm.org/10.1145/3450626.3459670)
  - [Code](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs)
  - Enables simulation of tight-tolerance assembly
  - Demonstrates sim-to-real transfer for peg insertion
```

#### Tools and Libraries

```markdown
- **[Tool Name](https://github.com/user/repo):** Brief description of functionality
  - Key feature 1
  - Key feature 2
```

**Example:**
```markdown
- **[skrl](https://github.com/Toni-SM/skrl):** Modular reinforcement learning library with Isaac Gym support
  - Compatible with Isaac Gym and Omniverse Isaac Gym
  - Provides PPO, SAC, TD3, and other algorithms
```

#### Tutorials and Guides

```markdown
- [Tutorial Title](https://url) - Brief description of what is covered
```

**Example:**
```markdown
- [Introduction to Isaac Gym](https://youtu.be/nleDq-oJjGk) - Getting started guide covering installation and basic concepts
```

---

## Pull Request Process

### Before You Submit

1. **Search existing content**: Ensure the resource is not already listed
2. **Check open PRs**: Someone may have already submitted what you want to add
3. **Verify the resource**: Confirm all links work and information is accurate

### Submitting Your PR

1. **Fork the repository** and create a new branch:
   ```bash
   git checkout -b add-resource-name
   ```

2. **Make your changes** following the [Style Guide](#style-guide)

3. **Commit with a clear message**:
   ```bash
   git commit -m "Add [Resource Name] to [Section Name]"
   ```

4. **Push and create a Pull Request**

### PR Description Template

Please include in your PR description:

```markdown
## Resource Addition

**Resource Name:** [Name]
**Category:** [Section where it should be added]
**URL:** [Link]

## Checklist

- [ ] I have verified all links work
- [ ] The resource is not already listed
- [ ] I have followed the formatting guidelines
- [ ] The resource meets the quality criteria
- [ ] I have added it to the appropriate section
```

### Review Process

1. A maintainer will review your PR within a few days
2. You may be asked to make changes or provide additional information
3. Once approved, your contribution will be merged
4. Thank you for improving this resource!

---

## Style Guide

### Markdown Formatting

- Use **ATX-style headers** (`#`, `##`, `###`)
- Use **hyphens** (`-`) for unordered lists
- Use **bold** (`**text**`) for resource names/titles
- Use **inline code** (`` `code` ``) for commands, file names, and technical terms
- Leave **one blank line** between sections
- Keep lines under **120 characters** when possible

### Link Formatting

- Use **descriptive link text** (avoid "click here" or raw URLs)
- Place **related links together** (paper, code, project page)
- Use **HTTPS** links when available

### Content Guidelines

- Write in **clear, concise English**
- Use **present tense** for descriptions
- Be **objective** - avoid promotional language
- Include **publication year** for papers and dated resources
- List **most recent or important items first** within sections

### Example of Good Formatting

```markdown
### Robot Manipulation

- **[RLAfford](https://github.com/hyperplane-lab/RLAfford):** End-to-end affordance learning with reinforcement learning (ICRA 2023)
  - [Paper](https://arxiv.org/abs/XXXX.XXXXX)
  - Learns object affordances directly from RL
  - Demonstrates generalization across object categories
```

---

## How the Research Bot Works

This repository includes an automated research bot that helps keep the "Latest Research" section up to date with newly published papers.

### What It Does

- **Searches arXiv** for papers related to Isaac Gym, Isaac Lab, and Omniverse Isaac
- **Runs daily** at 09:00 UTC via GitHub Actions
- **Creates draft PRs** with new paper entries for maintainer review
- **Updates content** between the `<!-- research-bot:start -->` and `<!-- research-bot:end -->` markers

### Important Notes

- The bot **never merges automatically** - all updates require maintainer approval
- Draft PRs are labeled with `bot` and `needs-approval`
- Manual triggers are available via the GitHub Actions "Research Bot" workflow

### Configuration

The bot is configured via `.research-bot.yaml`:

| Setting | Description | Default |
|---------|-------------|---------|
| `queries` | arXiv search terms | "isaac gym", "omni isaac", "isaac lab" |
| `days_back` | How far back to search | 7 days |
| `max_results` | Results per query | 25 |
| `output_count` | Max items in README | 10 |

### For Maintainers

To modify bot behavior:

1. Edit `.research-bot.yaml` in the repository root
2. Adjust search queries, time windows, or output limits as needed
3. Changes take effect on the next scheduled or manual run

---

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors.

### Our Standards

- **Be respectful**: Treat everyone with respect and consideration
- **Be constructive**: Provide helpful feedback and suggestions
- **Be inclusive**: Welcome contributors of all backgrounds and experience levels
- **Be collaborative**: Work together to improve the resource

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Personal attacks or inflammatory language
- Spam or self-promotion unrelated to the project
- Any other conduct that would be inappropriate in a professional setting

### Reporting

If you experience or witness unacceptable behavior, please open an issue or contact the maintainers directly. All reports will be handled with discretion.

---

## Questions and Contact

### Getting Help

- **General questions**: Open a [GitHub Discussion](../../discussions) or Issue
- **Bug reports**: Open an [Issue](../../issues) with details
- **Feature requests**: Open an Issue describing your idea

### Before Asking

1. Check the [README](README.md) for existing information
2. Search [existing issues](../../issues) for similar questions
3. Review [closed PRs](../../pulls?q=is%3Apr+is%3Aclosed) for context

### Response Times

- We aim to respond to issues and PRs within **3-5 business days**
- Complex contributions may take longer to review
- Please be patient - maintainers are volunteers

---

## Thank You!

Your contributions help make this resource valuable for the entire robotics and reinforcement learning community. Whether you are fixing a typo or suggesting a groundbreaking paper, every contribution matters.

We appreciate your time and effort in improving Awesome Isaac!
