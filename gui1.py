import sounddevice as sd
import numpy as np
import tkinter as tk
from tkinter import messagebox, font

# Parameters
duration = 5  # seconds
sample_rate = 44100  # Sample rate in Hz

class AudioRecorderApp:
    def __init__(self, master):
        self.master = master
        master.title("Audio Recorder")
        master.geometry("400x300")
        master.configure(bg="#e0f7fa")  # background color

        #custom font
        self.custom_font = font.Font(family="Helvetica", size=12)

        # Title Label
        self.title_label = tk.Label(master, text="Audio Recorder", bg="#e0f7fa", font=("Helvetica", 18, "bold"), fg="#00796b")
        self.title_label.pack(pady=20)

        # Record Button
        self.record_button = tk.Button(master, text="Record", command=self.record_audio, bg="#4db6ac", fg="white", font=self.custom_font, padx=20, pady=10, relief="flat")
        self.record_button.pack(pady=20)

        # RMS Label
        self.rms_label = tk.Label(master, text="RMS Value: ", bg="#e0f7fa", font=self.custom_font, fg="#004d40")
        self.rms_label.pack(pady=5)

        # Intensity Label
        self.intensity_label = tk.Label(master, text="Intensity (dB): ", bg="#e0f7fa", font=self.custom_font, fg="#004d40")
        self.intensity_label.pack(pady=5)

        # Exit Button
        self.exit_button = tk.Button(master, text="Exit", command=master.quit, bg="#ef5350", fg="white", font=self.custom_font, padx=20, pady=10, relief="flat")
        self.exit_button.pack(pady=20)

        # Add a footer label
        self.footer_label = tk.Label(master, text="Press 'Record' to start capturing audio.", bg="#e0f7fa", font=self.custom_font, fg="#00796b")
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def record_audio(self):
        print("Recording...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64')
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")

        # Calculate RMS (Root Mean Square)
        rms_value = np.sqrt(np.mean(np.square(audio_data)))

        # Convert RMS to decibels (optional)
        intensity_db = 20 * np.log10(rms_value) if rms_value > 0 else -np.inf

        # Update labels with results
        self.rms_label.config(text=f"RMS Value: {rms_value:.6f}")
        self.intensity_label.config(text=f"Intensity (dB): {intensity_db:.2f} dB")

        # Optionally show a message box with results
        messagebox.showinfo("Recording Finished", f"RMS Value: {rms_value:.6f}\nIntensity (dB): {intensity_db:.2f} dB")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioRecorderApp(root)
    root.mainloop()
