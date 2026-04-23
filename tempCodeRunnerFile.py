import customtkinter as ctk
from app import get_answer

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RashiGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rashi AI ✨")
        self.geometry("950x580")
        self.minsize(900, 550)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ========== SIDEBAR ==========
        self.sidebar = ctk.CTkFrame(
            self,
            width=240,
            corner_radius=30,
            fg_color="#7B6CFF"  # 💜 Purple
        )
        self.sidebar.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="❀ Rashi AI",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="white"
        )
        self.logo.pack(pady=(30, 6))

        self.tagline = ctk.CTkLabel(
            self.sidebar,
            text="Smart • Voice • Creative",
            font=ctk.CTkFont(size=13),
            text_color="#F3EFFF"
        )
        self.tagline.pack(pady=(0, 30))

        self.mode = ctk.StringVar(value="text")

        self.text_btn = ctk.CTkRadioButton(
            self.sidebar,
            text="💬 Text Chat",
            variable=self.mode,
            value="text",
            fg_color="#00F0FF",     # 💎 Neon Cyan
            hover_color="#00C9D6",
            text_color="white"
        )
        self.text_btn.pack(pady=14)

        self.voice_btn = ctk.CTkRadioButton(
            self.sidebar,
            text="🎤 Voice Chat",
            variable=self.mode,
            value="voice",
            fg_color="#FF8AD8",     # 💖 Pink
            hover_color="#FF5FC5",
            text_color="white"
        )
        self.voice_btn.pack(pady=14)

        self.status = ctk.CTkLabel(
            self.sidebar,
            text="● Ready",
            text_color="#D6FFFA",
            font=ctk.CTkFont(size=13)
        )
        self.status.pack(side="bottom", pady=25)

        # ========== CHAT AREA ==========
        self.chat_frame = ctk.CTkFrame(
            self,
            corner_radius=35,
            fg_color="#1B1E2E"  # 🌌 Navy
        )
        self.chat_frame.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")
        self.chat_frame.grid_rowconfigure(0, weight=1)
        self.chat_frame.grid_columnconfigure(0, weight=1)

        self.chat_box = ctk.CTkTextbox(
            self.chat_frame,
            font=("Segoe UI", 14),
            wrap="word",
            corner_radius=30,
            fg_color="#242842",
            text_color="#F5F6FF"
        )
        self.chat_box.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        self.chat_box.insert("end", "🌸 Rashi: Hey! Let’s chat 💖\n\n")
        self.chat_box.configure(state="disabled")

        # ========== INPUT ==========
        self.input_frame = ctk.CTkFrame(
            self,
            corner_radius=30,
            fg_color="#16192B"
        )
        self.input_frame.grid(row=1, column=1, padx=(0, 20), pady=(0, 20), sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)

        self.input_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Type something amazing…",
            fg_color="#0F1222",
            text_color="white",
            border_color="#FF8AD8",   # 💖 Pink border
            border_width=2
        )
        self.input_entry.grid(row=0, column=0, padx=25, pady=18, sticky="ew")
        self.input_entry.bind("<Return>", lambda e: self.send())

        self.send_btn = ctk.CTkButton(
            self.input_frame,
            text="Send ✨",
            width=140,
            fg_color="#00F0FF",      # 💎 Neon
            hover_color="#00C9D6",
            text_color="#0F1222",
            corner_radius=20,
            command=self.send
        )
        self.send_btn.grid(row=0, column=1, padx=18)

    # ========== LOGIC ==========
    def send(self):
        msg = self.input_entry.get().strip()
        if not msg:
            return

        self.input_entry.delete(0, "end")
        self.add_chat(f"🧑 You: {msg}\n")

        if self.mode.get() == "voice":
            self.add_chat("🎤 Voice mode selected\n\n")
            return

        self.status.configure(text="● Thinking…")
        self.update()

        reply = get_answer(msg)
        self.add_chat(f"🌸 Rashi: {reply}\n\n")
        self.status.configure(text="● Ready")

    def add_chat(self, text):
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", text)
        self.chat_box.see("end")
        self.chat_box.configure(state="disabled")


if __name__ == "__main__":
    app = RashiGUI()
    app.mainloop()