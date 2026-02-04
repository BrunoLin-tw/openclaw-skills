# openclaw-skills

A collection of skills for Clawdbot/Moltbot/Openclaw agents.

## Available Skills

| Skill | Description |
|-------|-------------|
| [ez-cronjob](./ez-cronjob) | Fix common cron job failures - message delivery, timeouts, timezone bugs |

## Installation

### Via ClawdHub

```bash
clawdhub install <skill-name>
```

### Manual

Copy the skill folder to your workspace or user skills directory:

```bash
# Workspace-level (single agent)
cp -r <skill-name> /path/to/workspace/skills/

# User-level (all agents)
cp -r <skill-name> ~/.openclaw/skills/
```

## Author

**Isaac Zarzuri** - [@Yz7hmpm](https://x.com/Yz7hmpm)

**Modified by Bruno Lin** - Added ez-cronjob skill and updated documentation.

Website: [metacognitivo.com](https://www.metacognitivo.com)

## License

MIT
