import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
import datetime

# ------------------------ LOGIN PAGE ------------------------ #
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Antrian Dealer Motor")
        self.root.geometry("300x200")
        self.root.configure(bg="#f5f5f5")

        self.frame = tk.Frame(self.root, padx=20, pady=20, bg="#f5f5f5")
        self.frame.pack(expand=True)

        tk.Label(self.frame, text="Login", font=("Helvetica", 16, "bold"), bg="#f5f5f5").pack(pady=10)

        tk.Label(self.frame, text="Username:", bg="#f5f5f5").pack(anchor="w")
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(fill="x", pady=5)

        tk.Label(self.frame, text="Password:", bg="#f5f5f5").pack(anchor="w")
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(fill="x", pady=5)

        tk.Button(self.frame, text="Login", bg="#4caf50", fg="white", command=self.cek_login).pack(pady=10, fill="x")

    def cek_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == "admin" and password == "1234":
            self.root.destroy()  # Tutup window login
            main_app()  # Panggil fungsi untuk buka app utama
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah!")

# -------------------- MAIN APPLICATION --------------------- #
class DealerQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Antrian Dealer Motor")
        self.root.geometry("600x750")
        self.root.configure(bg="#e8f0fe")

        self.antrian_motor = deque()
        self.riwayat_pelayanan = []

        self.frame = tk.Frame(root, padx=15, pady=15, bg="#e8f0fe")
        self.frame.pack(fill="both", expand=True)

        self.title = tk.Label(self.frame, text="🏍 Antrian Dealer Motor", font=("Helvetica", 18, "bold"), bg="#e8f0fe", fg="#333")
        self.title.pack(pady=10)

        # Input Nama
        self.nama_label = tk.Label(self.frame, text="Nama Pelanggan:", font=("Helvetica", 12), bg="#e8f0fe", fg="#333")
        self.nama_label.pack(anchor="w")
        self.nama_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.nama_entry.pack(fill="x", pady=5)

        # Separator
        ttk.Separator(self.frame, orient="horizontal").pack(fill="x", pady=5)

        # Input Plat
        self.plat_label = tk.Label(self.frame, text="Nomor Plat Kendaraan:", font=("Helvetica", 12), bg="#e8f0fe", fg="#333")
        self.plat_label.pack(anchor="w")
        self.plat_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.plat_entry.pack(fill="x", pady=5)

        ttk.Separator(self.frame, orient="horizontal").pack(fill="x", pady=5)

        # Input Telepon
        self.telepon_label = tk.Label(self.frame, text="Nomor Telepon:", font=("Helvetica", 12), bg="#e8f0fe", fg="#333")
        self.telepon_label.pack(anchor="w")
        self.telepon_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.telepon_entry.pack(fill="x", pady=5)

        ttk.Separator(self.frame, orient="horizontal").pack(fill="x", pady=5)

        # Input Keluhan
        self.keluhan_label = tk.Label(self.frame, text="Keluhan Kendaraan:", font=("Helvetica", 12), bg="#e8f0fe", fg="#333")
        self.keluhan_label.pack(anchor="w")
        self.keluhan_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.keluhan_entry.pack(fill="x", pady=5)

        ttk.Separator(self.frame, orient="horizontal").pack(fill="x", pady=5)

        # Tombol Tambah
        self.btn_tambah = tk.Button(self.frame, text="➕ Tambah ke Antrian", font=("Helvetica", 12), bg="#4caf50", fg="white",
                                    activebackground="#45a049", command=self.tambah_pelanggan)
        self.btn_tambah.pack(pady=10, fill="x")

        ttk.Separator(self.frame, orient="horizontal").pack(fill="x", pady=5)

        # Treeview
        columns = ("No", "Nama Pelanggan", "Nomor Plat", "Nomor Telepon", "Keluhan")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=12)
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "No":
                self.tree.column(col, width=40, anchor="center")
            elif col == "Nama Pelanggan":
                self.tree.column(col, width=180)
            elif col == "Nomor Plat":
                self.tree.column(col, width=120)
            elif col == "Nomor Telepon":
                self.tree.column(col, width=120)
            else:
                self.tree.column(col, width=240)
        self.tree.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Tombol Layani
        self.btn_layani_motor = tk.Button(self.frame, text="✅ Layani Pelanggan", font=("Helvetica", 12), bg="#2196f3", fg="white",
                                          activebackground="#1976d2", command=self.layani)
        self.btn_layani_motor.pack(pady=10, fill="x")

        ttk.Separator(self.frame, orient="horizontal").pack(fill="x", pady=5)

        # Estimasi & Progress
        self.estimasi_label = tk.Label(self.frame, text="", font=("Helvetica", 11, "italic"), fg="#666", bg="#e8f0fe")
        self.estimasi_label.pack(pady=5)

        self.progress = tk.Label(self.frame, text="", font=("Helvetica", 12), fg="green", bg="#e8f0fe")
        self.progress.pack(pady=5)

        ttk.Separator(self.frame, orient="horizontal").pack(fill="x", pady=10)

        # Hapus
        self.hapus_label = tk.Label(self.frame, text="Hapus Pelanggan", font=("Helvetica", 14, "bold"), bg="#e8f0fe", fg="#333")
        self.hapus_label.pack(pady=(0, 5))

        self.hapus_nama_label = tk.Label(self.frame, text="Nama Pelanggan:", font=("Helvetica", 12), bg="#e8f0fe", fg="#333")
        self.hapus_nama_label.pack(anchor="w")
        self.hapus_nama_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.hapus_nama_entry.pack(fill="x", pady=5)

        self.btn_hapus = tk.Button(self.frame, text="❌ Hapus Pelanggan", font=("Helvetica", 12), bg="#f44336", fg="white",
                                   activebackground="#d32f2f", command=self.hapus_pelanggan)
        self.btn_hapus.pack(pady=10, fill="x")

        ttk.Separator(self.frame, orient="horizontal").pack(fill="x", pady=10)

        self.btn_reset = tk.Button(self.frame, text="🔄 Reset Semua Antrian & Riwayat", font=("Helvetica", 12), bg="#9e9e9e", fg="white",
                                   activebackground="#757575", command=self.reset_semua)
        self.btn_reset.pack(pady=10, fill="x")

        self.btn_keluar = tk.Button(self.frame, text="❌ Keluar", font=("Helvetica", 12), bg="#607d8b", fg="white",
                                   activebackground="#455a64", command=root.quit)
        self.btn_keluar.pack(pady=10, fill="x")

        self.perbarui_tampilan()

    def perbarui_tampilan(self):
        self.tree.delete(*self.tree.get_children())
        for i, (nama, plat, telepon, keluhan) in enumerate(self.antrian_motor, start=1):
            self.tree.insert("", "end", values=(i, nama, plat, telepon, keluhan))
        total = len(self.antrian_motor)
        self.progress.config(text=f"📈 Total pelanggan dalam antrian: {total}")
        self.estimasi_label.config(text=f"⏳ Estimasi waktu tunggu: ~{total * 5} menit")

    def tambah_pelanggan(self):
        nama = self.nama_entry.get().strip()
        plat = self.plat_entry.get().strip()
        telepon = self.telepon_entry.get().strip()
        keluhan = self.keluhan_entry.get().strip()

        if not all([nama, plat, telepon]):
            messagebox.showwarning("Input Kosong", "Mohon lengkapi semua data.")
            return

        if any(nama == n for n, _, _, _ in self.antrian_motor):
            messagebox.showwarning("Duplikat Nama", f"Nama '{nama}' sudah ada dalam antrian.")
            return

        self.antrian_motor.append((nama, plat, telepon, keluhan))
        self.nama_entry.delete(0, tk.END)
        self.plat_entry.delete(0, tk.END)
        self.telepon_entry.delete(0, tk.END)
        self.keluhan_entry.delete(0, tk.END)
        self.perbarui_tampilan()

    def layani(self):
        if self.antrian_motor:
            nama, plat, telepon, _ = self.antrian_motor.popleft()
            self.catat_pelayanan(nama)
            messagebox.showinfo("Dilayani", f"{nama} dengan plat {plat} telah dilayani.")
        else:
            messagebox.showinfo("Kosong", "Tidak ada pelanggan.")
        self.perbarui_tampilan()

    def catat_pelayanan(self, nama):
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.riwayat_pelayanan.append({"waktu": waktu, "nama": nama, "jenis": "Motor"})

    def hapus_pelanggan(self):
        nama = self.hapus_nama_entry.get().strip()
        for p in list(self.antrian_motor):
            if p[0] == nama:
                self.antrian_motor.remove(p)
                messagebox.showinfo("Berhasil", f"Pelanggan '{nama}' dihapus.")
                self.hapus_nama_entry.delete(0, tk.END)
                self.perbarui_tampilan()
                return
        messagebox.showwarning("Tidak Ditemukan", f"'{nama}' tidak ada dalam antrian.")

    def reset_semua(self):
        if messagebox.askyesno("Konfirmasi", "Yakin ingin mereset semua?"):
            self.antrian_motor.clear()
            self.riwayat_pelayanan.clear()
            self.perbarui_tampilan()

# ------------------------ MAIN ------------------------ #
def main_app():
    root = tk.Tk()
    app = DealerQueueApp(root)
    root.mainloop()

if __name__ == "__main__":
    login_root = tk.Tk()
    login = LoginWindow(login_root)
    login_root.mainloop()
