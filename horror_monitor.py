import tkinter as tk
import random
import time
import math

message = [
    "ТЫ ОДИН.",
    "МОЛИСЬ И ВЕРЬ.",
    "Ты не смог."
]
tag_name = [
    "ТЫ ОДИН.",
    "Оно наблюдает.",
    "Слышишь шепот?",
    "Закрой глаза.",
    "Не оборачивайся.",
    "Оно уже здесь.",
    "Оно внутри.",
    "Тело не твое.",
    "Не доверяй своим глазам.",
    "ГДЕ-ТО РЯДОМ ОНО.",
    "Найди его.",
    "Найди ключ."
]
BG_COLOR = "#0A0000"
FG_COLOR_NORMAL = "#00FF00"
FG_COLOR_WARNING = "#FFFF00"
FG_COLOR_ALERT = "#FFA500"
FG_COLOR_CRITICAL = "#FF0000"
FG_COLOR_UNKNOWN = "#800080"
FONT_FAMILY = "Courier New"
FONT_SIZE_NORMAL = 12
FONT_SIZE_LARGE = 14
BORDER_COLOR_NORMAL = "#330000"
BORDER_COLOR_CRITICAL = "#FF0000"
BORDER_WIDTH = 1
PAD_X = 5
PAD_Y = 5
UPDATE_INTERVAL_MS = 500


SENSOR_NAMES = [
    "Signal Integrity [dB]",
    "Anomaly Signature [Units]",
    "Containment Pressure [kPa]",
    "Energy Flux [GW]",
    "Neural Pattern [Correlation]",
    "Structural Stress [%]",
    "System Corruption [%]"
]

MESSAGE_TYPES = { 
    "[LOG]": FG_COLOR_NORMAL,
    "[DATA]": FG_COLOR_NORMAL,
    "[WARNING]": FG_COLOR_WARNING,
    "[ALERT]": FG_COLOR_ALERT,
    "[ERROR]": FG_COLOR_CRITICAL,
    "[BREACH]": FG_COLOR_CRITICAL,
    "[UNKNOWN]": FG_COLOR_UNKNOWN,
    "[CORRUPTION]": FG_COLOR_UNKNOWN
}

MESSAGE_FRAGMENTS = [
    "INTEGRITY COMPROMISED", "BREACH IMMINENT", "UNAUTHORIZED ACCESS DETECTED", "STRANGE SIGNAL ORIGINATING INTERNALLY",
    "CANNOT CONTAIN ANOMALY", "LOST CONTACT WITH UNIT", "DATA CORRUPTION DETECTED", "PATTERN MATCH: KETER-CLASS EVENT",
    "PRESSURE RISING CRITICALLY", "ENERGY DRAIN UNEXPLAINED", "NEURAL ACTIVITY SPIKE (NON-HUMAN)", "STRUCTURAL FAILURE IMMINENT",
    "SYSTEM OVERLOAD", "SECURITY PROTOCOLS FAILING", "EXTRACTING DATA (UNKNOWN SOURCE)", "SILENCE ON ALL CHANNELS",
    "THE WALLS ARE WEAKENING", "IT'S INSIDE THE PERIMETER", "CONTINGENCY PLAN OMEGA INITIATED", "NO RESPONSE FROM CONTROL",
    "GRAVITY FLUCTUATIONS", "DIMENSIONAL SHEAR DETECTED", "REALITY DEVIATION 0.03%", "AUDITORY HALLUCINATIONS REPORTED",
    "VISUAL DISTORTIONS INCREASING", "TEMPORAL DISPLACEMENT MINOR", "ISOLATION PROTOCOL FAILED", "UNKNOWN ENTITY REGISTERED"
]

STATUS_NAMES = [
    "Subsystem Alpha",
    "Neural Interface",
    "Containment Unit",
    "Processing Core",
    "Transmission Array",
    "Life Support"
]
STATUS_VALUES = ["ONLINE", "OFFLINE", "WARNING", "CRITICAL", "COMPROMISED", "BREACHED", "CORRUPTED", "UNKNOWN"]


class MysteriousMonitor:
    def add_message(self):
        pass
    def update_messages(self):
        pass


    def __init__(self, root):
        self.root = root
        root.title("Monitoring Station // Status: UNSTABLE")
        root.geometry("1000x700")
        root.configure(bg=BG_COLOR)

        
        root.grid_columnconfigure(0, weight=1, uniform="group1")
        root.grid_columnconfigure(1, weight=1, uniform="group1")
        root.grid_rowconfigure(0, weight=1, uniform="group1")
        root.grid_rowconfigure(1, weight=2, uniform="group1")
        root.grid_rowconfigure(2, weight=1, uniform="group1")




        self.sensor_frame = tk.Frame(root, bg=BG_COLOR, bd=BORDER_WIDTH, relief="solid", highlightbackground=BORDER_COLOR_NORMAL, highlightthickness=BORDER_WIDTH)
        self.sensor_frame.grid(row=0, column=0, sticky="nsew", padx=PAD_X, pady=PAD_Y)
        self.sensor_frame.grid_columnconfigure(0, weight=1)
        self.sensor_labels = {}
        tk.Label(self.sensor_frame, text="[ ANOMALY READINGS ]", bg=BG_COLOR, fg=FG_COLOR_ALERT, font=(FONT_FAMILY, FONT_SIZE_LARGE, "bold")).pack(pady=(5, 0))
        for i, name in enumerate(SENSOR_NAMES):
            label = tk.Label(self.sensor_frame, text=f"{name}: --", bg=BG_COLOR, fg=FG_COLOR_NORMAL, font=(FONT_FAMILY, FONT_SIZE_NORMAL))
            label.pack(anchor="w", padx=10)
            self.sensor_labels[name] = label


        self.graph_frame = tk.Frame(root, bg=BG_COLOR, bd=BORDER_WIDTH, relief="solid", highlightbackground=BORDER_COLOR_NORMAL, highlightthickness=BORDER_WIDTH)
        self.graph_frame.grid(row=0, column=1, sticky="nsew", padx=PAD_X, pady=PAD_Y)
        self.graph_frame.grid_columnconfigure(0, weight=1)
        self.graph_frame.grid_rowconfigure(1, weight=1)
        tk.Label(self.graph_frame, text="[ ACTIVITY SPIKES ]", bg=BG_COLOR, fg=FG_COLOR_ALERT, font=(FONT_FAMILY, FONT_SIZE_LARGE, "bold")).grid(row=0, column=0, pady=(5, 0))
        self.graph_canvas = tk.Canvas(self.graph_frame, bg=BG_COLOR, highlightthickness=0)
        self.graph_canvas.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.graph_data = [random.uniform(20, 40)] * 100 # Больше точек для графика, более низкое начальное значение
        self.graph_max_points = 100


        self.message_frame = tk.Frame(root, bg=BG_COLOR, bd=BORDER_WIDTH, relief="solid", highlightbackground=BORDER_COLOR_NORMAL, highlightthickness=BORDER_WIDTH)
        self.message_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=PAD_X, pady=PAD_Y)
        self.message_frame.grid_columnconfigure(0, weight=1)
        self.message_frame.grid_rowconfigure(1, weight=1)
        tk.Label(self.message_frame, text="[ SYSTEM LOG / ALERTS ]", bg=BG_COLOR, fg=FG_COLOR_ALERT, font=(FONT_FAMILY, FONT_SIZE_LARGE, "bold")).grid(row=0, column=0, pady=(5, 0))
        self.message_text = tk.Text(self.message_frame, bg=BG_COLOR, fg=FG_COLOR_NORMAL, font=(FONT_FAMILY, FONT_SIZE_NORMAL), state='disabled', wrap='word', highlightthickness=0)
        self.message_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)


        for msg_type, color in MESSAGE_TYPES.items():
             tag_name = msg_type.strip("[]").lower()
             self.message_text.tag_config(tag_name, foreground=color)




        self.status_frame = tk.Frame(root, bg=BG_COLOR, bd=BORDER_WIDTH, relief="solid", highlightbackground=BORDER_COLOR_NORMAL, highlightthickness=BORDER_WIDTH)
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=PAD_X, pady=PAD_Y)

        num_status_cols = min(len(STATUS_NAMES), 3)
        for i in range(num_status_cols):
             self.status_frame.grid_columnconfigure(i, weight=1)

        tk.Label(self.status_frame, text="[ SUBSYSTEM STATUS ]", bg=BG_COLOR, fg=FG_COLOR_ALERT, font=(FONT_FAMILY, FONT_SIZE_LARGE, "bold")).grid(row=0, column=0, columnspan=num_status_cols, pady=(5, 0))
        self.status_labels = {}
        for i, name in enumerate(STATUS_NAMES):
            row = (i // num_status_cols) + 1
            col = i % num_status_cols
            label = tk.Label(self.status_frame, text=f"{name}: --", bg=BG_COLOR, fg=FG_COLOR_NORMAL, font=(FONT_FAMILY, FONT_SIZE_NORMAL))
            label.grid(row=row, column=col, sticky="w", padx=10)
            self.status_labels[name] = label


        self.containment_integrity = 100.0
        self.corruption_level = 0.0
        self.breach_imminent = False
        self.critical_event_active = False


        self.update_data()

    def update_data(self):

        self.simulate_events()
        self.update_sensor_readings()
        self.update_graph()
        self.update_messages()
        self.update_statuses()
        self.update_title()


        self.root.after(UPDATE_INTERVAL_MS, self.update_data)

    def simulate_events(self):

        decay_rate = random.uniform(0.001, 0.01)
        self.containment_integrity -= decay_rate
        if random.random() < 0.02:
             self.containment_integrity -= random.uniform(0.1, 1.0)
        if random.random() < 0.005:
             self.containment_integrity -= random.uniform(2.0, 10.0)

        self.containment_integrity = max(0.0, self.containment_integrity)


        corruption_increase = random.uniform(0.005, 0.05)
        self.corruption_level += corruption_increase
        if random.random() < 0.01:
             self.corruption_level += random.uniform(0.5, 5.0)
        self.corruption_level = min(100.0, self.corruption_level)


        if not self.critical_event_active and (self.containment_integrity < 20 or self.corruption_level > 80 or random.random() < 0.002): # Высокий уровень опасности или очень низкий шанс
             self.critical_event_active = True
             self.breach_imminent = True
             self.add_message("[ALERT]", "CRITICAL EVENT DETECTED - BREACH IMMINENT")
             self.add_message("[ERROR]", "AUTOMATED CONTAINMENT PROTOCOLS FAILING")


        if self.breach_imminent:
             self.containment_integrity -= random.uniform(0.5, 2.0)
             self.corruption_level += random.uniform(0.5, 2.0)
             self.containment_integrity = max(0.0, self.containment_integrity)
             self.corruption_level = min(100.0, self.corruption_level)
             if self.containment_integrity <= 0.01 and self.corruption_level >= 99.9:

                  if not hasattr(self, 'final_message_shown'):
                       self.add_message("[BREACH]", "CONTAINMENT FAILURE - ALL SYSTEMS COMPROMISED")
                       self.add_message("[BREACH]", "REALITY DEVIATION CRITICAL - EVACUATE IMMEDIATELY")
                       self.root.title("Monitoring Station // Status: OFFLINE (COMPROMISED)")

                       self.final_message_shown = True


    def update_sensor_readings(self):

        for name in SENSOR_NAMES:
            value = 0.0

            if "Signal Integrity" in name:

                base = random.uniform(50.0, 100.0)
                noise = random.uniform(-10, 10)
                corruption_penalty = self.corruption_level * random.uniform(0.2, 0.5)
                value = base + noise - corruption_penalty
                value = max(0.0, value)

            elif "Anomaly Signature" in name:

                 base = random.uniform(0.0, 5.0)
                 anomaly_spike_chance = 0.1 + (100 - self.containment_integrity) / 200
                 if random.random() < anomaly_spike_chance:
                      base += random.uniform(5.0, 30.0)
                 value = base
                 if self.breach_imminent:
                      value += random.uniform(20.0, 100.0)

            elif "Containment Pressure" in name:

                 base = random.uniform(95.0, 105.0)
                 integrity_effect = (100 - self.containment_integrity) * random.uniform(0.05, 0.2)
                 value = base - integrity_effect + random.uniform(-2, 2)
                 value = max(0.0, value)

            elif "Energy Flux" in name:

                 base = random.uniform(1.0, 10.0)
                 spike_chance = 0.05 + (self.corruption_level / 300)
                 if random.random() < spike_chance:
                      base += random.uniform(10.0, 60.0)
                 if self.critical_event_active:
                      base += random.uniform(20.0, 100.0)
                 value = base
                 value = max(0.0, value)

            elif "Neural Pattern" in name:

                 base = random.uniform(40.0, 60.0)
                 anomaly_effect = self.sensor_labels.get("Anomaly Signature [Units]", None)
                 if anomaly_effect and ":" in anomaly_effect.cget("text"):
                      try:
                           current_anomaly = float(anomaly_effect.cget("text").split(":")[1].strip())
                           base += current_anomaly * random.uniform(0.1, 0.5)
                      except ValueError:
                           pass
                 noise = random.uniform(-5, 5)
                 value = base + noise
                 value = max(0.0, value)


            elif "Structural Stress" in name:

                 base = random.uniform(0.0, 5.0)
                 integrity_effect = (100 - self.containment_integrity) * random.uniform(0.1, 0.3)
                 pressure_effect = self.sensor_labels.get("Containment Pressure [kPa]", None)
                 energy_effect = self.sensor_labels.get("Energy Flux [GW]", None)
                 if pressure_effect and ":" in pressure_effect.cget("text"):
                      try:
                           p_val = float(pressure_effect.cget("text").split(":")[1].strip())
                           if p_val > 100: base += (p_val - 100) * random.uniform(0.1, 0.5)
                      except ValueError: pass
                 if energy_effect and ":" in energy_effect.cget("text"):
                      try:
                           e_val = float(energy_effect.cget("text").split(":")[1].strip())
                           if e_val > 20: base += (e_val - 20) * random.uniform(0.05, 0.3)
                      except ValueError: pass

                 value = base + integrity_effect + random.uniform(-1, 1)
                 value = max(0.0, value)
                 value = min(100.0, value)

            elif "System Corruption" in name:

                 value = self.corruption_level

            else:
                value = random.uniform(0, 100)


            color = FG_COLOR_NORMAL
            if "Integrity" in name or "Containment" in name:
                 if value < 10: color = FG_COLOR_CRITICAL
                 elif value < 30: color = FG_COLOR_ALERT
                 elif value < 60: color = FG_COLOR_WARNING
            elif "Anomaly" in name or "Energy" in name or "Structural" in name:
                 if value > 50: color = FG_COLOR_CRITICAL
                 elif value > 30: color = FG_COLOR_ALERT
                 elif value > 10: color = FG_COLOR_WARNING
            elif "Corruption" in name:
                 if value > 80: color = FG_COLOR_CRITICAL
                 elif value > 50: color = FG_COLOR_ALERT
                 elif value > 20: color = FG_COLOR_WARNING


            self.sensor_labels[name].config(text=f"{name}: {value:.2f}", fg=color)


    def update_graph(self):

        anomaly_label = self.sensor_labels.get("Anomaly Signature [Units]", None)
        current_anomaly = 0.0
        if anomaly_label and ":" in anomaly_label.cget("text"):
             try:
                 current_anomaly = float(anomaly_label.cget("text").split(":")[1].strip())
             except ValueError:
                 pass


             last_value = self.graph_data[-1]

             scaled_anomaly = min(100, current_anomaly * 2)
             change = random.uniform(-5, 5) + (scaled_anomaly - last_value) * random.uniform(0.05,
                                                                                             0.1)

             new_value = last_value + change + (random.random() > 0.9) * random.uniform(-20,
                                                                                        20)
             new_value = max(0, min(100, new_value))

             self.graph_data.append(new_value)


             if len(self.graph_data) > self.graph_max_points:
                 self.graph_data.pop(0)


             self.graph_canvas.delete("all")

             width = self.graph_canvas.winfo_width()
             height = self.graph_canvas.winfo_height()

             if width <= 1 or height <= 1:
                 return


             points = []
             max_val = 100
             min_val = 0
             data_range = max_val - min_val

             if data_range <= 0: data_range = 1


             avg_value = sum(self.graph_data) / len(self.graph_data) if self.graph_data else 0
             line_color = FG_COLOR_NORMAL
             if avg_value > 70 or self.graph_data[-1] > 80:
                 line_color = FG_COLOR_CRITICAL
             elif avg_value > 50 or self.graph_data[-1] > 60:
                 line_color = FG_COLOR_ALERT
             elif avg_value > 30 or self.graph_data[-1] > 40:
                 line_color = FG_COLOR_WARNING

             for i, value in enumerate(self.graph_data):

                 y = height - ((value - min_val) / data_range) * height

                 x = (i / (len(self.graph_data) - 1)) * width if len(self.graph_data) > 1 else 0
                 points.append((x, y))

             if len(points) > 1:
                 self.graph_canvas.create_line(points, fill=line_color, width=1)

        def update_messages(self):

            if random.random() < 0.4:
                return

            timestamp = time.strftime("%H:%M:%S")


            msg_type = random.choices(list(MESSAGE_TYPES.keys()), weights=[10, 10, 20, 20, 15, 10, 10, 5], k=1)[
                0]

            fragment1 = random.choice(MESSAGE_FRAGMENTS)
            fragment2 = random.choice(MESSAGE_FRAGMENTS) if random.random() > 0.6 else ""  # Чаще два фрагмента

            message_text = f"[{timestamp}] {msg_type}: {fragment1} {fragment2}".strip()
            message_text += "\n"

            tag_name = msg_type.strip("[]").lower()
            self.add_message(tag_name, message_text)

        def add_message(self, tag_name, message):
            """Добавляет сообщение в текстовое поле с указанным тегом."""
        self.message_text.config(state='normal')
        self.message_text.insert(tk.END, message, tag_name)
        self.message_text.see(tk.END)
        self.message_text.config(state='disabled')


        max_lines = 150
        current_lines = int(self.message_text.index('end-1c').split('.')[0])
        if current_lines > max_lines:
             self.message_text.config(state='normal')
             lines_to_delete = current_lines - max_lines
             self.message_text.delete(1.0, f'{lines_to_delete + 1}.0')
             self.message_text.config(state='disabled')


    def update_statuses(self):

        for name in STATUS_NAMES:

            status = "ONLINE"
            color = FG_COLOR_NORMAL
            prob = random.random()


            if prob < 0.05:
                 status = random.choice(["CRITICAL", "BREACHED"])
            elif prob < 0.15:
                 status = random.choice(["OFFLINE", "CORRUPTED"])
            elif prob < 0.35:
                 status = random.choice(["WARNING", "COMPROMISED"])
            elif prob < 0.40:
                 status = "UNKNOWN"




            if self.critical_event_active:
                 if "Containment" in name or "Life Support" in name:
                      status = random.choice(["CRITICAL", "BREACHED", "OFFLINE"])
                 elif "Neural" in name or "Processing" in name:
                      status = random.choice(["CRITICAL", "CORRUPTED", "COMPROMISED"])


            if self.corruption_level > 50 and random.random() < (self.corruption_level - 50) / 100:
                 status = random.choice(["CORRUPTED", "UNKNOWN", "OFFLINE", "CRITICAL"])
            if self.breach_imminent:
                 status = random.choice(["BREACHED", "CRITICAL", "OFFLINE", "COMPROMISED"])



            if status == "CRITICAL" or status == "OFFLINE" or status == "BREACHED":
                color = FG_COLOR_CRITICAL
            elif status == "WARNING" or status == "COMPROMISED":
                color = FG_COLOR_ALERT
            elif status == "CORRUPTED" or status == "UNKNOWN":
                 color = FG_COLOR_UNKNOWN
            else: # ONLINE
                 color = FG_COLOR_NORMAL


            self.status_labels[name].config(text=f"{name}: {status}", fg=color)


        critical_statuses = ["CRITICAL", "OFFLINE", "BREACHED", "CORRUPTED"]
        any_critical = any(self.status_labels[name].cget("text").split(": ")[1] in critical_statuses for name in STATUS_NAMES)
        self.status_frame.config(highlightbackground=BORDER_COLOR_CRITICAL if any_critical else BORDER_COLOR_NORMAL)
        self.sensor_frame.config(highlightbackground=BORDER_COLOR_CRITICAL if any_critical or self.containment_integrity < 30 or self.corruption_level > 70 else BORDER_COLOR_NORMAL)
        self.graph_frame.config(highlightbackground=BORDER_COLOR_CRITICAL if any_critical or self.graph_data[-1] > 80 else BORDER_COLOR_NORMAL)
        self.message_frame.config(highlightbackground=BORDER_COLOR_CRITICAL if any_critical else BORDER_COLOR_NORMAL)


    def update_title(self):

        if self.breach_imminent:
             self.root.title("Monitoring Station // Status: BREACH DETECTED")
        elif self.critical_event_active:
             self.root.title("Monitoring Station // Status: CRITICAL EVENT")
        elif self.containment_integrity < 50 or self.corruption_level > 50:
             self.root.title("Monitoring Station // Status: UNSTABLE")
        else:
             self.root.title("Monitoring Station // Status: MONITORING")


# ЗАПУСК
if 1 == 1:
    root = tk.Tk()
    app = MysteriousMonitor(root)
    root.mainloop()
