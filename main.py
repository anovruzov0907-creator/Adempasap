import random
import string
import tkinter as tk
from tkinter import messagebox
import os

# Fayl yolu (S22 Ultra yaddaşı)
FAYL_YOLU = "/sdcard/Documents/adem_sifreler.txt"

def sifre_yarat():
    try:
        uzunluq = int(length_entry.get())
        platforma = platform_entry.get().strip()
        
        if not platforma:
            messagebox.showwarning("Diqqət", "Platforma adını qeyd edin!")
            return

        simvollar = string.ascii_letters + string.digits + "!@#$%^&*"
        sifre = ''.join(random.choice(simvollar) for _ in range(uzunluq))
        
        # Nəticəni yenilə
        result_label.config(text=sifre)
        
        # Fayla yaz
        with open(FAYL_YOLU, "a", encoding="utf-8") as f:
            f.write(f"[{platforma}] -> {sifre}\n")
            
    except ValueError:
        messagebox.showerror("Xəta", "Uzunluq rəqəm olmalıdır!")

def kopyala():
    sifre = result_label.cget("text")
    if sifre:
        root.clipboard_clear()
        root.clipboard_append(sifre)
        messagebox.showinfo("Uğurlu", "Şifrə kopyalandı!")
    else:
        messagebox.showwarning("Xəta", "Əvvəlcə şifrə yaradın!")

def kohne_sifreler():
    pencere = tk.Toplevel(root)
    pencere.title("Arxiv")
    pencere.geometry("350x500")
    pencere.configure(bg="#121212")
    
    tk.Label(pencere, text="KEÇMİŞ ŞİFRƏLƏR", fg="#BB86FC", bg="#121212", font=("Helvetica", 12, "bold")).pack(pady=10)
    
    txt = tk.Text(pencere, bg="#1E1E1E", fg="#03DAC6", font=("Consolas", 10), bd=0, padx=10, pady=10)
    txt.pack(expand=True, fill="both", padx=15, pady=15)
    
    if os.path.exists(FAYL_YOLU):
        with open(FAYL_YOLU, "r", encoding="utf-8") as f:
            txt.insert("1.0", f.read())
    else:
        txt.insert("1.0", "Hələ ki heç bir şifrə saxlanılmayıb.")
    txt.config(state="disabled")

# Əsas Pəncərə Dizaynı
root = tk.Tk()
root.title("ADEM M-PASS")
root.geometry("380x600")
root.configure(bg="#0F0F0F")

# Başlıq Dizaynı (BMW Mavisi)
tk.Label(root, text="/// M-PERFORMANCE", fg="#1E88E5", bg="#0F0F0F", font=("Verdana", 16, "bold italic")).pack(pady=25)

# Platforma Sahəsi
tk.Label(root, text="PLATFORMA", fg="#AAAAAA", bg="#0F0F0F", font=("Helvetica", 9, "bold")).pack()
platform_entry = tk.Entry(root, bg="#1E1E1E", fg="white", insertbackground="white", font=("Helvetica", 12), border=0, justify="center")
platform_entry.pack(pady=10, ipady=8, padx=50, fill="x")

# Uzunluq Sahəsi
tk.Label(root, text="ŞİFRƏ UZUNLUĞU", fg="#AAAAAA", bg="#0F0F0F", font=("Helvetica", 9, "bold")).pack(pady=5)
length_entry = tk.Entry(root, bg="#1E1E1E", fg="white", insertbackground="white", font=("Helvetica", 12), border=0, justify="center")
length_entry.insert(0, "16")
length_entry.pack(pady=10, ipady=8, padx=120, fill="x")

# Əsas Düymə (BMW M-Sport Mavisi)
yarat_btn = tk.Button(root, text="YARAT VƏ SAXLA", command=sifre_yarat, bg="#1E88E5", fg="white", font=("Helvetica", 11, "bold"), bd=0, cursor="hand2")
yarat_btn.pack(pady=20, ipady=12, padx=50, fill="x")

# Şifrə Nəticəsi (Neon Yaşıl)
result_label = tk.Label(root, text="", fg="#03DAC6", bg="#0F0F0F", font=("Consolas", 16, "bold"), wraplength=300)
result_label.pack(pady=15)

# Kopyala Düyməsi
kopyala_btn = tk.Button(root, text="KOPYALA", command=kopyala, bg="#3700B3", fg="white", font=("Helvetica", 10, "bold"), bd=0)
kopyala_btn.pack(pady=5, ipady=8, padx=80, fill="x")

# Arxiv Düyməsi (Tünd Boz)
arxiv_btn = tk.Button(root, text="ARXİVƏ BAX", command=kohne_sifreler, bg="#333333", fg="#CCCCCC", font=("Helvetica", 9), bd=0)
arxiv_btn.pack(side="bottom", pady=30, ipady=5, padx=100, fill="x")

root.mainloop()
