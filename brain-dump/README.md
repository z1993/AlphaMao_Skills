# Brain Dump Skill 🧠

An intelligent orchestrator for Obsidian that transforms chaotic user thoughts into structured notes with tasks, ideas, thoughts, and emotions.

## 🌟 Features

- **Brain to Vault**: Instantly captures stream-of-consciousness input.
- **Auto-Sorting**: Automatically categorizes content into Actions, Ideas, Thoughts, and Emotions.
- **Obsidian Native**: Generates beautifully formatted Markdown files directly in your vault.
- **Smart Dashboard**: Automatically creates and updates a "Brain Dump Dashboard" to visualize your mental state.

## 🚀 Installation & Setup

1. **Install the Skill**:
   Clone this repository into your skill directory.

2. **Obsidian Configuration (Critical Step)**:
   This skill works best with the **Dataview** plugin in Obsidian to power the Dashboard.
   
   - **Install Dataview**: Open Obsidian > Settings > Community Plugins > Browse > Search "Dataview" > Install & Enable.
   - **File Path**: The skill is configured to save files to: `[Insert Your Obsidian Vault Path Here]\Brain Dumps\`. 
     > **Note**: You MUST edit `SKILL.md` to match your actual Obsidian vault path.

3. **Dashboard Initialization**:
   The first time you run the skill, it will automatically create a `Brain Dump Dashboard.md` file in the target directory. This dashboard uses Dataview queries to show your recent tasks, ideas, and emotional trends.

## 📖 Usage

Simply tell the agent:
> "Brain dump: I need to buy milk, I have an idea for a new app, and I'm feeling great today."

The agent will:
1. Parse your input.
2. Sort it into categories (Actions, Ideas, Thoughts, Emotions).
3. Create a new daily note (e.g., `2026-01-23_BrainDump_Milk_App.md`).
4. Update your Dashboard view.

## 📂 Output Structure

Each dump creates a file with this structure:

```markdown
# Brain Dump - 2026-01-23

## ✅ Actions
- [ ] Buy milk #todo

## 💡 Ideas
- New app concept #idea

## 💭 Thoughts
- Reflection on the day #thought

## ❤️ Emotions
- Feeling great #emotion
```

## 🙏 Acknowledgements

Special thanks to the **Obsidian Skill** community and the **Obsidian** team for building such a powerful knowledge base tool. This skill is built to extend the capabilities of Obsidian as a second brain.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License
