\# LLM-Screen-Bridge



A Python-based automation tool that bridges on-screen content with any AI LLM of your choice. It captures a specific region of the screen defined by UI markers (that you choose) and sends the data to an LLM for task solving and interaction.



\## ℹ️ How it Works

1\. \*\*Detection:\*\* Locates `top\_element.png` (top left anchor) and `bottom\_element.png` (bottom right anchor) to define the capture area.

2\. \*\*Analysis:\*\* Captures the screen and sends it to the AI for screen analysis and interaction.

3\. \*\*Execution:\*\* The AI returns click coordinates, which the script executes automatically.

4\. \*\*Loop:\*\* The program automatically repeats - it sends the next screenshot to the AI for further interaction.



\## 🛠️ Requirements

\* Python 3.x

\* Required libraries: `pip install -r requirements.txt`



\## ⚠️ Safety Features

AI can misbehave, so it is best to keep watch - if you find that it starts doing things you don't want it to, you can hold the `ESC` key at any time to kill the script.



\## 📜 License

This project is licensed under the GNU GPLv3.

✅ Commercial Use

✅ Modification

✅ Distribution

❌ Closed Source Distribution

❌ Changing the License

❌ Holding Authors Liable

⚠️ Disclose Source

⚠️ Include License Notice

⚠️ Apply Same License to Derivatives

