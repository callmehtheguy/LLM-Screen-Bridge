# LLM-Screen-Bridge

A Python-based automation tool that bridges on-screen content with any AI LLM of your choice. It captures a specific region of the screen defined by UI markers (that you choose) and sends the data to an LLM for task solving and interaction.


## ℹ️ How it Works

1. **Calibration:** You move your mouse to locations of your choice to define the capture area - this is the area that the AI will be limited to.

2. **Analysis:** Captures the screen and sends it to the AI for screen analysis and interaction. Compatible with almost all LLMs.

3. **Execution:** The AI returns click coordinates, which the script executes automatically.

4. **Loop:** The program automatically repeats - it sends the next screenshot to the AI for further interaction.


## 🛠️ Setup

1. **Install the program:** Head to https://download-directory.github.io/ to install the files. Extract them.


2. **Prepare Images:** Prepare the following images and name them the following:


   `ask_ai.png` - The placeholder text for the textbox in a conversation with the AI of your choosing.
   <img width="240" height="242" alt="image" src="https://github.com/user-attachments/assets/dffaf65a-b6e0-4947-a510-813ea908a2ee" />


   `copy_text_button.png` - The "Copy text" button
   <img width="329" height="378" alt="image" src="https://github.com/user-attachments/assets/f2e70066-0a24-4619-b3a0-1869d579626f" />


3. **Install required libraries:** Run `pip install -r requirements.txt` in the command prompt.
  

4. **Run the .py script:** Run the script and follow the instructions within the script.


Need help? Discord @callmehtheguy; Gmail callmehtheguy@gmail.com


## ✅ Requirements

* Python 3.x

* Required libraries: `pip install -r requirements.txt`



## ⚠️ Safety Information

* AI can misbehave, so it is best to keep watch - if you find that it starts doing things you don't want it to, you can hold the `ESC` key at any time to kill the script.

* This tool automates mouse and keyboard inputs. Use at your own risk. The author is not responsible for any damage caused by actions taken by any AI.


## 📜 License

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

