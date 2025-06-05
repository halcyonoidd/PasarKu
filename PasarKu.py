import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Listbox, StringVar, END
from abc import ABC, abstractmethod

STYLE = {
    "bg_main": "#f7f9fc",
    "fg_main": "#1f2d3d",
    "font_title": ("Segoe UI", 18, "bold"),
    "font_normal": ("Segoe UI", 11),
    "btn_primary": {"bg": "#3498db", "fg": "white"},
    "btn_success": {"bg": "#2ecc71", "fg": "white"},
    "btn_danger": {"bg": "#e74c3c", "fg": "white"},
    "btn_default": {"bg": "#7f8c8d", "fg": "white"},
    "pad_y": 8,
    "pad_x": 20,
    "entry_width": 35
}

def apply_label_style(label, title=False):
    label.config(bg=STYLE["bg_main"], fg=STYLE["fg_main"], font=STYLE["font_title"] if title else STYLE["font_normal"])

def apply_button_style(button, style="default"):
    s = STYLE.get(f"btn_{style}", STYLE["btn_default"])
    button.config(bg=s["bg"], fg=s["fg"], font=STYLE["font_normal"], width=25, pady=5)

def apply_entry_style(entry):
    entry.config(font=STYLE["font_normal"], width=STYLE["entry_width"])






# --- Abstraksi, Inheritance/SuperClass, setter getter, enkapsulasi(semuanya bertipe protected), dan overriding ---

class User(ABC):
    def __init__(self, email, password, alamat, no_telepon):
        self._email = email # enkapsulasi - protected
        self._password = password
        self._alamat = alamat
        self._no_telepon = no_telepon

    def get_email(self): return self._email #getter
    def get_password(self): return self._password
    def get_alamat(self): return self._alamat
    def get_no_telepon(self): return self._no_telepon
    def set_alamat(self, alamat): self._alamat = alamat #setter
    def set_no_telepon(self, no_telepon): self._no_telepon = no_telepon

    @abstractmethod #abstraksi
    def show_menu(self): pass 


class Product(ABC):
    def __init__(self, id_produk, nama, harga, stok, ukuran, penjual_email):
        self._id_produk = id_produk
        self._nama = nama
        self._harga = harga
        self._stok = stok
        self._ukuran = ukuran
        self._penjual_email = penjual_email

    def get_id_produk(self): return self._id_produk
    def get_nama(self): return self._nama
    def get_harga(self): return self._harga
    def get_stok(self): return self._stok
    def get_ukuran(self): return self._ukuran
    def get_penjual_email(self): return self._penjual_email

    def set_nama(self, nama): self._nama = nama
    def set_harga(self, harga): self._harga = harga
    def set_stok(self, stok): self._stok = stok
    def set_ukuran(self, ukuran): self._ukuran = ukuran

    @abstractmethod
    def show_info(self): pass #overriding

    @abstractmethod
    def get_kategori(self): pass






# --- Inheritance/Subclass Produk ---

class Miscellaneous(Product):
    def __init__(self, id_produk, nama, harga, stok, ukuran, bahan, penjual_email):
        super().__init__(id_produk, nama, harga, stok, ukuran, penjual_email)
        self._bahan = bahan

    def get_bahan(self): return self._bahan
    def set_bahan(self, bahan): self._bahan = bahan

    def show_info(self): #overriding
        return f"ID: {self.get_id_produk()}\nNama: {self.get_nama()}\nHarga: Rp{self.get_harga():,}\nStok: {self.get_stok()}\nUkuran: {self.get_ukuran()}\nBahan: {self._bahan}"

    def get_kategori(self): return "Miscellaneous"


class Elektronik(Product):
    def __init__(self, id_produk, nama, harga, stok, ukuran, daya, kapasitas, material, penjual_email):
        super().__init__(id_produk, nama, harga, stok, ukuran, penjual_email)
        self._daya = daya
        self._kapasitas = kapasitas
        self._material = material

    def get_daya(self): return self._daya
    def get_kapasitas(self): return self._kapasitas
    def get_material(self): return self._material
    def set_daya(self, daya): self._daya = daya
    def set_kapasitas(self, kapasitas): self._kapasitas = kapasitas
    def set_material(self, material): self._material = material

    def show_info(self):
        return f"ID: {self.get_id_produk()}\nNama: {self.get_nama()}\nHarga: Rp{self.get_harga():,}\nStok: {self.get_stok()}\nUkuran: {self.get_ukuran()}\nDaya: {self._daya}\nKapasitas: {self._kapasitas}\nMaterial: {self._material}"

    def get_kategori(self): return "Elektronik"


class Pakaian(Product):
    def __init__(self, id_produk, nama, harga, stok, ukuran, bahan, penjual_email):
        super().__init__(id_produk, nama, harga, stok, ukuran, penjual_email)
        self._bahan = bahan

    def get_bahan(self): return self._bahan
    def set_bahan(self, bahan): self._bahan = bahan

    def show_info(self):
        return f"ID: {self.get_id_produk()}\nNama: {self.get_nama()}\nHarga: Rp{self.get_harga():,}\nStok: {self.get_stok()}\nUkuran: {self.get_ukuran()}\nBahan: {self._bahan}"

    def get_kategori(self): return "Pakaian"






# --- Subclass User ---

class Penjual(User):
    def __init__(self, email, password, alamat, no_telepon, nama_toko):
        super().__init__(email, password, alamat, no_telepon)
        self._nama_toko = nama_toko

    def get_nama_toko(self): return self._nama_toko
    def set_nama_toko(self, nama_toko): self._nama_toko = nama_toko

    def show_menu(self): pass


class Pembeli(User):
    def __init__(self, email, password, alamat, no_telepon):
        super().__init__(email, password, alamat, no_telepon)
        self._keranjang = []

    def get_keranjang(self): return self._keranjang

    def tambah_ke_keranjang(self, produk, jumlah):
        for item in self._keranjang:
            if item["produk"].get_id_produk() == produk.get_id_produk():
                item["jumlah"] += jumlah
                return
        self._keranjang.append({"produk": produk, "jumlah": jumlah})

    def hapus_dari_keranjang(self, id_produk):
        self._keranjang = [item for item in self._keranjang if item["produk"].get_id_produk() != id_produk]

    def show_menu(self): pass






# --- Pesanan ---

class Pesanan:
    def __init__(self, id_pesanan, pembeli_email, produk, jumlah, metode_pembayaran, status="Pending"):
        self._id_pesanan = id_pesanan
        self._pembeli_email = pembeli_email
        self._produk = produk
        self._jumlah = jumlah
        self._metode_pembayaran = metode_pembayaran
        self._status = status

    def get_id_pesanan(self): return self._id_pesanan
    def get_pembeli_email(self): return self._pembeli_email
    def get_produk(self): return self._produk
    def get_jumlah(self): return self._jumlah
    def get_metode_pembayaran(self): return self._metode_pembayaran
    def get_status(self): return self._status
    def set_status(self, status): self._status = status
    def get_total_harga(self): return self._produk.get_harga() * self._jumlah


class SistemJualBeli:
    def __init__(self):
        self._users = {}
        self._products = []
        self._pesanan = []
        self._current_user = None
        self._next_product_id = 1
        self._next_order_id = 1

    def get_current_user(self): return self._current_user
    def set_current_user(self, user): self._current_user = user
    def get_users(self): return self._users
    def get_products(self): return self._products
    def get_pesanan(self): return self._pesanan

    def get_products_by_category(self, kategori):
        return [p for p in self._products if p.get_kategori() == kategori]

    def get_products_by_seller(self, penjual_email):
        return [p for p in self._products if p.get_penjual_email() == penjual_email]

    def get_sellers(self):
        return [user for user in self._users.values() if isinstance(user, Penjual)]

    def get_penjual_by_email(self, email):
        return self._users.get(email)

    def get_penjual_by_nama_toko(self, nama_toko):
        for user in self.get_sellers():
            if user.get_nama_toko() == nama_toko:
                return user
        return None

    def buat_pesanan(self, produk, jumlah, metode_pembayaran):
        if produk.get_stok() < jumlah:
            return False, "Stok tidak mencukupi!"
        pesanan = Pesanan(self._next_order_id, self._current_user.get_email(), produk, jumlah, metode_pembayaran)
        self._pesanan.append(pesanan)
        produk.set_stok(produk.get_stok() - jumlah)
        self._next_order_id += 1
        return True, f"Pesanan berhasil dibuat!\nTotal: Rp{pesanan.get_total_harga():,}\nMetode Pembayaran: {metode_pembayaran}"






# --- GUI ---

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PasarKu - Sistem E-Commerce Sederhana")
        self.root.geometry("800x600")
        self.root.configure(bg=STYLE["bg_main"])
        self.sistem = SistemJualBeli()
        self.show_role_menu()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_role_menu(self):
        self.clear()
        frame = tk.Frame(self.root, bg=STYLE["bg_main"])
        frame.pack(expand=True)
        title_frame = tk.Frame(frame, bg=STYLE["bg_main"])
        title_frame.pack(pady=(30, 10))
        title = tk.Label(title_frame, text="PasarKu", font=STYLE["font_title"], bg=STYLE["bg_main"], fg=STYLE["fg_main"])
        logo = tk.Label(title_frame, text="🛒", font=("Segoe UI Emoji", 24), bg=STYLE["bg_main"])
        title.pack(side="left")
        logo.pack(side="left", padx=(10, 0))
        welcome = tk.Label(frame, text="Selamat datang di PasarKu! silahkan login sebagai:")
        apply_label_style(welcome)
        welcome.pack(pady=(0, 30))
        opsi_frame = tk.Frame(frame, bg=STYLE["bg_main"])
        opsi_frame.pack()
        penjual_box = tk.Frame(opsi_frame, bg="#e0e7ef", bd=2, relief="groove")
        penjual_box.grid(row=0, column=0, padx=20, pady=10)
        penjual_inner = tk.Frame(penjual_box, bg="#e0e7ef")
        penjual_inner.pack(padx=10, pady=10)
        toko_logo = tk.Label(penjual_inner, text="🏬", font=("Segoe UI Emoji", 18), bg="#e0e7ef")
        toko_logo.pack(side="left", padx=(0, 8))
        btn1 = tk.Button(penjual_inner, text="Penjual", command=lambda: self.show_login("penjual"))
        apply_button_style(btn1, "primary")
        btn1.pack(side="left")
        pembeli_box = tk.Frame(opsi_frame, bg="#e0e7ef", bd=2, relief="groove")
        pembeli_box.grid(row=0, column=1, padx=20, pady=10)
        pembeli_inner = tk.Frame(pembeli_box, bg="#e0e7ef")
        pembeli_inner.pack(padx=10, pady=10)
        keranjang_logo = tk.Label(pembeli_inner, text="🛒", font=("Segoe UI Emoji", 18), bg="#e0e7ef")
        keranjang_logo.pack(side="left", padx=(0, 8))
        btn2 = tk.Button(pembeli_inner, text="Pembeli", command=lambda: self.show_login("pembeli"))
        apply_button_style(btn2, "success")
        btn2.pack(side="left")
        btn3 = tk.Button(frame, text="Keluar", command=self.root.quit)
        apply_button_style(btn3, "danger")
        btn3.pack(pady=STYLE["pad_y"])

    def show_login(self, role):
        self.clear()
        frame = tk.Frame(self.root, bg=STYLE["bg_main"])
        frame.pack(expand=True)
        title_frame = tk.Frame(frame, bg=STYLE["bg_main"])
        title_frame.pack(pady=(10, 0))
        label = tk.Label(title_frame, text=f"Login {role.capitalize()}")
        apply_label_style(label, title=True)
        label.pack(side="left")
        lock_logo = tk.Label(title_frame, text="🔒", font=("Segoe UI Emoji", 18), bg=STYLE["bg_main"])
        lock_logo.pack(side="left", padx=(10, 0))
        email_var = tk.StringVar()
        pass_var = tk.StringVar()
        l1 = tk.Label(frame, text="Email:")
        apply_label_style(l1)
        l1.pack()
        e1 = tk.Entry(frame, textvariable=email_var)
        apply_entry_style(e1)
        e1.pack(pady=(0, STYLE["pad_y"]))
        l2 = tk.Label(frame, text="Password:")
        apply_label_style(l2)
        l2.pack()
        e2 = tk.Entry(frame, textvariable=pass_var, show="*")
        apply_entry_style(e2)
        e2.pack(pady=(0, STYLE["pad_y"]))
        def do_login():
            email = email_var.get()
            password = pass_var.get()
            users = self.sistem.get_users()
            if email in users and users[email].get_password() == password:
                user = users[email]
                if (role == "penjual" and isinstance(user, Penjual)) or (role == "pembeli" and isinstance(user, Pembeli)):
                    self.sistem.set_current_user(user)
                    if role == "penjual":
                        self.show_penjual_menu()
                    else:
                        self.show_pembeli_menu()
                else:
                    messagebox.showerror("Login", f"Akun ini bukan {role}!")
            else:
                messagebox.showerror("Login", "Email atau password salah!")
        btn = tk.Button(frame, text="Login", command=do_login)
        apply_button_style(btn, "primary")
        btn.pack(pady=STYLE["pad_y"])
        reg = tk.Button(frame, text="Belum punya akun? Daftar", command=lambda: self.show_register(role))
        apply_button_style(reg, "default")
        reg.pack()
        back = tk.Button(frame, text="⬅️ Kembali", command=self.show_role_menu)
        apply_button_style(back, "danger")
        back.pack(pady=STYLE["pad_y"])

    def show_register(self, role):
        self.clear()
        frame = tk.Frame(self.root, bg=STYLE["bg_main"])
        frame.pack(expand=True)
        title_frame = tk.Frame(frame, bg=STYLE["bg_main"])
        title_frame.pack(pady=(10, 0))
        label = tk.Label(title_frame, text=f"Daftar {role.capitalize()}")
        apply_label_style(label, title=True)
        label.pack(side="left")
        doc_logo = tk.Label(title_frame, text="📄", font=("Segoe UI Emoji", 18), bg=STYLE["bg_main"])
        doc_logo.pack(side="left", padx=(10, 0))
        email_var = tk.StringVar()
        pass_var = tk.StringVar()
        alamat_var = tk.StringVar()
        telp_var = tk.StringVar()
        nama_toko_var = tk.StringVar()
        for text, var in [("Email:", email_var), ("Password:", pass_var), ("Alamat:", alamat_var), ("No. Telepon:", telp_var)]:
            l = tk.Label(frame, text=text)
            apply_label_style(l)
            l.pack()
            e = tk.Entry(frame, textvariable=var, show="*" if text == "Password:" else None)
            apply_entry_style(e)
            e.pack(pady=(0, STYLE["pad_y"]))
        nama_toko_label = tk.Label(frame, text="Nama Toko:")
        apply_label_style(nama_toko_label)
        nama_toko_entry = tk.Entry(frame, textvariable=nama_toko_var)
        apply_entry_style(nama_toko_entry)
        if role == "penjual":
            nama_toko_label.pack()
            nama_toko_entry.pack(pady=(0, STYLE["pad_y"]))
        def do_register():
            email = email_var.get().strip()
            password = pass_var.get().strip()
            alamat = alamat_var.get().strip()
            telp = telp_var.get().strip()
            users = self.sistem.get_users()
            if not email or not password:
                messagebox.showerror("Register", "Email dan password tidak boleh kosong!")
                return
            if email in users:
                messagebox.showerror("Register", "Email sudah terdaftar!")
                return
            if role == "penjual":
                nama_toko = nama_toko_var.get().strip()
                if not nama_toko:
                    messagebox.showerror("Register", "Nama toko tidak boleh kosong!")
                    return
                user = Penjual(email, password, alamat, telp, nama_toko)
            else:
                user = Pembeli(email, password, alamat, telp)
            users[email] = user
            messagebox.showinfo("Register", "Registrasi berhasil!")
            self.show_login(role)
        btn = tk.Button(frame, text="Daftar", command=do_register)
        apply_button_style(btn, "primary")
        btn.pack(pady=STYLE["pad_y"])
        back = tk.Button(frame, text="⬅️ Kembali", command=lambda: self.show_login(role))
        apply_button_style(back, "danger")
        back.pack(pady=STYLE["pad_y"])






# --- Menu Penjual ---
    def show_penjual_menu(self):
        self.clear()
        frame = tk.Frame(self.root, bg=STYLE["bg_main"])
        frame.pack(expand=True)
        title_frame = tk.Frame(frame, bg=STYLE["bg_main"])
        title_frame.pack(pady=(10, 0))
        label = tk.Label(title_frame, text="Dashboard Penjual", font=STYLE["font_title"], bg=STYLE["bg_main"], fg=STYLE["fg_main"])
        label.pack(side="left")
        toko_logo = tk.Label(title_frame, text="🏬", font=("Segoe UI Emoji", 22), bg=STYLE["bg_main"])
        toko_logo.pack(side="left", padx=(10, 0))
        welcome = tk.Label(
            frame,
            text="Selamat beraktivitas! Saatnya buat tokomu makin dikenal dan dicari banyak pembeli."
        )
        apply_label_style(welcome)
        welcome.pack(pady=(0, 20))
        opsi_frame = tk.Frame(frame, bg=STYLE["bg_main"])
        opsi_frame.pack()
        kelola_box = tk.Frame(opsi_frame, bg="#3498db", bd=2, relief="groove")
        kelola_box.pack(pady=6, fill="x")
        kelola_inner = tk.Frame(kelola_box, bg="#3498db")
        kelola_inner.pack(padx=6, pady=6, fill="x")
        paket_logo = tk.Label(kelola_inner, text="📦", font=("Segoe UI Emoji", 14), bg="#3498db", fg="white")
        paket_logo.pack(side="left", padx=(0, 6))
        btn1 = tk.Button(
            kelola_inner, text="Kelola Produk", command=self.kelola_produk,
            bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn1.pack(side="left", fill="x", expand=True)
        proses_box = tk.Frame(opsi_frame, bg="#2ecc71", bd=2, relief="groove")
        proses_box.pack(pady=6, fill="x")
        proses_inner = tk.Frame(proses_box, bg="#2ecc71")
        proses_inner.pack(padx=6, pady=6, fill="x")
        mobil_logo = tk.Label(proses_inner, text="🚚", font=("Segoe UI Emoji", 14), bg="#2ecc71", fg="white")
        mobil_logo.pack(side="left", padx=(0, 6))
        btn2 = tk.Button(
            proses_inner, text="Proses Pesanan", command=self.proses_pesanan,
            bg="#2ecc71", fg="white", activebackground="#27ae60", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn2.pack(side="left", fill="x", expand=True)
        logout_box = tk.Frame(opsi_frame, bg="#e74c3c", bd=2, relief="groove")
        logout_box.pack(pady=6, fill="x")
        logout_inner = tk.Frame(logout_box, bg="#e74c3c")
        logout_inner.pack(padx=6, pady=6, fill="x")
        x_logo = tk.Label(logout_inner, text="❌", font=("Segoe UI Emoji", 14), bg="#e74c3c", fg="white")
        x_logo.pack(side="left", padx=(0, 6))
        btn3 = tk.Button(
            logout_inner, text="Logout", command=self.show_role_menu,
            bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn3.pack(side="left", fill="x", expand=True)

    def kelola_produk(self):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title("Kelola Produk")
        penjual = self.sistem.get_current_user()
        produk_saya = self.sistem.get_products_by_seller(penjual.get_email())
        label = tk.Label(win, text="Daftar Produk Anda:")
        apply_label_style(label)
        label.pack(pady=10)
        listbox = Listbox(win, width=60)
        listbox.pack(pady=10)
        for p in produk_saya:
            listbox.insert(END, f"{p.get_nama()} | Stok: {p.get_stok()} | Rp{p.get_harga():,}")

        def tambah_produk():
            tambah_win = Toplevel(win, bg=STYLE["bg_main"])
            tambah_win.title("Tambah Produk")
            label = tk.Label(tambah_win, text="Tambah Produk Baru")
            apply_label_style(label, title=True)
            label.pack(pady=10)
            kategori_var = StringVar(value="Miscellaneous")
            kategori_label = tk.Label(tambah_win, text="Kategori:")
            apply_label_style(kategori_label)
            kategori_label.pack()
            kategori_menu = tk.OptionMenu(tambah_win, kategori_var, "Miscellaneous", "Elektronik", "Pakaian")
            kategori_menu.pack()
            nama_var = StringVar()
            harga_var = StringVar()
            stok_var = StringVar()
            ukuran_var = StringVar()
            for text, var in [("Nama:", nama_var), ("Harga:", harga_var), ("Stok:", stok_var), ("Ukuran:", ukuran_var)]:
                l = tk.Label(tambah_win, text=text)
                apply_label_style(l)
                l.pack()
                e = tk.Entry(tambah_win, textvariable=var)
                apply_entry_style(e)
                e.pack(pady=(0, STYLE["pad_y"]))
            extra_frame = tk.Frame(tambah_win, bg=STYLE["bg_main"])
            extra_frame.pack()
            extra_var1 = StringVar()
            extra_var2 = StringVar()
            extra_var3 = StringVar()
            def update_fields(*args):
                for widget in extra_frame.winfo_children():
                    widget.destroy()
                if kategori_var.get() == "Miscellaneous":
                    l = tk.Label(extra_frame, text="Bahan:")
                    apply_label_style(l)
                    l.pack()
                    e = tk.Entry(extra_frame, textvariable=extra_var1)
                    apply_entry_style(e)
                    e.pack()
                    extra_var2.set("")
                    extra_var3.set("")
                elif kategori_var.get() == "Elektronik":
                    for text, var in [("Daya:", extra_var1), ("Kapasitas:", extra_var2), ("Material:", extra_var3)]:
                        l = tk.Label(extra_frame, text=text)
                        apply_label_style(l)
                        l.pack()
                        e = tk.Entry(extra_frame, textvariable=var)
                        apply_entry_style(e)
                        e.pack()
                elif kategori_var.get() == "Pakaian":
                    l = tk.Label(extra_frame, text="Bahan:")
                    apply_label_style(l)
                    l.pack()
                    e = tk.Entry(extra_frame, textvariable=extra_var1)
                    apply_entry_style(e)
                    e.pack()
                    extra_var2.set("")
                    extra_var3.set("")
            kategori_var.trace("w", update_fields)
            update_fields()
            def simpan():
                nama = nama_var.get()
                try:
                    harga = int(harga_var.get())
                    stok = int(stok_var.get())
                except:
                    messagebox.showerror("Input", "Harga dan stok harus angka!", parent=tambah_win)
                    return
                ukuran = ukuran_var.get()
                kategori = kategori_var.get()
                pid = len(self.sistem.get_products()) + 1
                if kategori == "Miscellaneous":
                    produk = Miscellaneous(pid, nama, harga, stok, ukuran, extra_var1.get(), penjual.get_email())
                elif kategori == "Elektronik":
                    produk = Elektronik(pid, nama, harga, stok, ukuran, extra_var1.get(), extra_var2.get(), extra_var3.get(), penjual.get_email())
                elif kategori == "Pakaian":
                    produk = Pakaian(pid, nama, harga, stok, ukuran, extra_var1.get(), penjual.get_email())
                self.sistem.get_products().append(produk)
                messagebox.showinfo("Tambah", "Produk berhasil ditambahkan!", parent=tambah_win)
                tambah_win.destroy()
                win.destroy()
                self.kelola_produk()
            btn = tk.Button(tambah_win, text="Simpan", command=simpan)
            apply_button_style(btn, "primary")
            btn.pack(pady=STYLE["pad_y"])


        def hapus_produk():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Produk", "Pilih produk yang akan dihapus!", parent=win)
                return
            produk = produk_saya[idx[0]]
            pesanan_aktif = [
                p for p in self.sistem.get_pesanan()
                if p.get_produk().get_id_produk() == produk.get_id_produk() and p.get_status() in ("Pending", "Dikirim")
            ]
            if pesanan_aktif:
                messagebox.showwarning("Tidak Bisa Dihapus", "Produk sedang dalam proses transaksi dan tidak bisa dihapus!", parent=win)
                return
            self.sistem.get_products().remove(produk)
            messagebox.showinfo("Hapus", "Produk berhasil dihapus!", parent=win)
            win.destroy()
            self.kelola_produk()


        def edit_produk():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Produk", "Pilih produk yang akan diedit!", parent=win)
                return
            produk = produk_saya[idx[0]]
            edit_win = Toplevel(win, bg=STYLE["bg_main"])
            edit_win.title("Edit Produk")
            label = tk.Label(edit_win, text="Edit Produk")
            apply_label_style(label, title=True)
            label.pack(pady=10)
            nama_var = StringVar(value=produk.get_nama())
            harga_var = StringVar(value=str(produk.get_harga()))
            stok_var = StringVar(value=str(produk.get_stok()))
            ukuran_var = StringVar(value=produk.get_ukuran())
            for text, var in [("Nama:", nama_var), ("Harga:", harga_var), ("Stok:", stok_var), ("Ukuran:", ukuran_var)]:
                l = tk.Label(edit_win, text=text)
                apply_label_style(l)
                l.pack()
                e = tk.Entry(edit_win, textvariable=var)
                apply_entry_style(e)
                e.pack(pady=(0, STYLE["pad_y"]))
            extra_frame = tk.Frame(edit_win, bg=STYLE["bg_main"])
            extra_frame.pack()
            extra_var1 = StringVar()
            extra_var2 = StringVar()
            extra_var3 = StringVar()
            if isinstance(produk, Miscellaneous):
                extra_var1.set(produk.get_bahan())
                l = tk.Label(extra_frame, text="Bahan:")
                apply_label_style(l)
                l.pack()
                e = tk.Entry(extra_frame, textvariable=extra_var1)
                apply_entry_style(e)
                e.pack()
            elif isinstance(produk, Elektronik):
                extra_var1.set(produk.get_daya())
                extra_var2.set(produk.get_kapasitas())
                extra_var3.set(produk.get_material())
                for text, var in [("Daya:", extra_var1), ("Kapasitas:", extra_var2), ("Material:", extra_var3)]:
                    l = tk.Label(extra_frame, text=text)
                    apply_label_style(l)
                    l.pack()
                    e = tk.Entry(extra_frame, textvariable=var)
                    apply_entry_style(e)
                    e.pack()
            elif isinstance(produk, Pakaian):
                extra_var1.set(produk.get_bahan())
                l = tk.Label(extra_frame, text="Bahan:")
                apply_label_style(l)
                l.pack()
                e = tk.Entry(extra_frame, textvariable=extra_var1)
                apply_entry_style(e)
                e.pack()
            def simpan():
                produk.set_nama(nama_var.get())
                produk.set_harga(int(harga_var.get()))
                produk.set_stok(int(stok_var.get()))
                produk.set_ukuran(ukuran_var.get())
                if isinstance(produk, Miscellaneous):
                    produk.set_bahan(extra_var1.get())
                elif isinstance(produk, Elektronik):
                    produk.set_daya(extra_var1.get())
                    produk.set_kapasitas(extra_var2.get())
                    produk.set_material(extra_var3.get())
                elif isinstance(produk, Pakaian):
                    produk.set_bahan(extra_var1.get())
                messagebox.showinfo("Edit", "Produk berhasil diupdate!", parent=edit_win)
                edit_win.destroy()
                win.destroy()
                self.kelola_produk()
            btn = tk.Button(edit_win, text="Simpan", command=simpan)
            apply_button_style(btn, "primary")
            btn.pack(pady=STYLE["pad_y"])

        btn_tambah = tk.Button(win, text="Tambah Produk", command=tambah_produk)
        apply_button_style(btn_tambah, "primary")
        btn_tambah.pack(pady=STYLE["pad_y"])
        btn_edit = tk.Button(win, text="Edit Produk", command=edit_produk)
        apply_button_style(btn_edit, "success")
        btn_edit.pack(pady=STYLE["pad_y"])
        btn_hapus = tk.Button(win, text="Hapus Produk", command=hapus_produk)
        apply_button_style(btn_hapus, "danger")
        btn_hapus.pack(pady=STYLE["pad_y"])
        btn_tutup = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn_tutup, "default")
        btn_tutup.pack(pady=STYLE["pad_y"])


    def proses_pesanan(self):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title("Proses Pesanan")
        penjual = self.sistem.get_current_user()
        pesanan_saya = [p for p in self.sistem.get_pesanan() if p.get_produk().get_penjual_email() == penjual.get_email() and p.get_status() == "Pending"]
        label = tk.Label(win, text="Pesanan Masuk:")
        apply_label_style(label)
        label.pack(pady=10)
        listbox = Listbox(win, width=80)
        listbox.pack(pady=10)
        for p in pesanan_saya:
            listbox.insert(END, f"{p.get_produk().get_nama()} | Jumlah: {p.get_jumlah()} | Total: Rp{p.get_total_harga():,} | Status: {p.get_status()}")
        def proses():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Pesanan", "Pilih pesanan!", parent=win)
                return
            pesanan = pesanan_saya[idx[0]]
            aksi_win = Toplevel(win, bg=STYLE["bg_main"])
            aksi_win.title("Aksi Pesanan")
            label = tk.Label(aksi_win, text=f"Pesanan: {pesanan.get_produk().get_nama()}\nJumlah: {pesanan.get_jumlah()}\nStatus: {pesanan.get_status()}")
            apply_label_style(label)
            label.pack(pady=10)
            def kirim():
                pesanan.set_status("Dikirim")
                messagebox.showinfo("Pesanan", "Pesanan berhasil dikirim!", parent=aksi_win)
                aksi_win.destroy()
                win.destroy()
                self.proses_pesanan()
            def batal():
                pesanan.set_status("Dibatalkan")
                produk = pesanan.get_produk()
                produk.set_stok(produk.get_stok() + pesanan.get_jumlah())
                messagebox.showinfo("Pesanan", "Pesanan berhasil dibatalkan!", parent=aksi_win)
                aksi_win.destroy()
                win.destroy()
                self.proses_pesanan()
            btn_kirim = tk.Button(aksi_win, text="Kirim Pesanan", command=kirim)
            apply_button_style(btn_kirim, "primary")
            btn_kirim.pack(pady=STYLE["pad_y"])
            btn_batal = tk.Button(aksi_win, text="Batalkan Pesanan", command=batal)
            apply_button_style(btn_batal, "danger")
            btn_batal.pack(pady=STYLE["pad_y"])
            btn_tutup = tk.Button(aksi_win, text="Tutup", command=aksi_win.destroy)
            apply_button_style(btn_tutup, "default")
            btn_tutup.pack(pady=STYLE["pad_y"])
        btn_proses = tk.Button(win, text="Proses Pesanan", command=proses)
        apply_button_style(btn_proses, "primary")
        btn_proses.pack(pady=STYLE["pad_y"])
        btn_tutup = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn_tutup, "default")
        btn_tutup.pack(pady=STYLE["pad_y"])


# --- Menu Pembeli ---
    def show_pembeli_menu(self):
        self.clear()
        frame = tk.Frame(self.root, bg=STYLE["bg_main"])
        frame.pack(expand=True)
        title_frame = tk.Frame(frame, bg=STYLE["bg_main"])
        title_frame.pack(pady=(10, 0))
        label = tk.Label(title_frame, text="Dashboard Pembeli", font=STYLE["font_title"], bg=STYLE["bg_main"], fg=STYLE["fg_main"])
        label.pack(side="left")
        keranjang_logo = tk.Label(title_frame, text="🛒", font=("Segoe UI Emoji", 22), bg=STYLE["bg_main"])
        keranjang_logo.pack(side="left", padx=(10, 0))
        welcome = tk.Label(frame, text="Selamat berbelanja! Nikmati pengalaman belanja terbaik bersama kami.")
        apply_label_style(welcome)
        welcome.pack(pady=(0, 20))
        opsi_frame = tk.Frame(frame, bg=STYLE["bg_main"])
        opsi_frame.pack()
        cari_box = tk.Frame(opsi_frame, bg="#3498db", bd=2, relief="groove")
        cari_box.pack(pady=6, fill="x")
        cari_inner = tk.Frame(cari_box, bg="#3498db")
        cari_inner.pack(padx=6, pady=6, fill="x")
        kaca_logo = tk.Label(cari_inner, text="🔍", font=("Segoe UI Emoji", 14), bg="#3498db", fg="white")
        kaca_logo.pack(side="left", padx=(0, 6))
        btn1 = tk.Button(
            cari_inner, text="Cari Produk", command=self.menu_cari_produk,
            bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn1.pack(side="left", fill="x", expand=True)
        toko_box = tk.Frame(opsi_frame, bg="#2ecc71", bd=2, relief="groove")
        toko_box.pack(pady=6, fill="x")
        toko_inner = tk.Frame(toko_box, bg="#2ecc71")
        toko_inner.pack(padx=6, pady=6, fill="x")
        toko_logo = tk.Label(toko_inner, text="🏬", font=("Segoe UI Emoji", 14), bg="#2ecc71", fg="white")
        toko_logo.pack(side="left", padx=(0, 6))
        btn2 = tk.Button(
            toko_inner, text="Lihat Toko", command=self.menu_cari_toko,
            bg="#2ecc71", fg="white", activebackground="#27ae60", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn2.pack(side="left", fill="x", expand=True)
        keranjang_box = tk.Frame(opsi_frame, bg="#7f8c8d", bd=2, relief="groove")
        keranjang_box.pack(pady=6, fill="x")
        keranjang_inner = tk.Frame(keranjang_box, bg="#7f8c8d")
        keranjang_inner.pack(padx=6, pady=6, fill="x")
        keranjang_logo2 = tk.Label(keranjang_inner, text="🛒", font=("Segoe UI Emoji", 14), bg="#7f8c8d", fg="white")
        keranjang_logo2.pack(side="left", padx=(0, 6))
        btn3 = tk.Button(
            keranjang_inner, text="Keranjang", command=self.show_keranjang,
            bg="#7f8c8d", fg="white", activebackground="#636e72", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn3.pack(side="left", fill="x", expand=True)
        pesanan_box = tk.Frame(opsi_frame, bg="#3498db", bd=2, relief="groove")
        pesanan_box.pack(pady=6, fill="x")
        pesanan_inner = tk.Frame(pesanan_box, bg="#3498db")
        pesanan_inner.pack(padx=6, pady=6, fill="x")
        kardus_logo = tk.Label(pesanan_inner, text="📦", font=("Segoe UI Emoji", 14), bg="#3498db", fg="white")
        kardus_logo.pack(side="left", padx=(0, 6))
        btn4 = tk.Button(
            pesanan_inner, text="Daftar Pesanan", command=self.show_daftar_pesanan,
            bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn4.pack(side="left", fill="x", expand=True)
        history_box = tk.Frame(opsi_frame, bg="#2ecc71", bd=2, relief="groove")
        history_box.pack(pady=6, fill="x")
        history_inner = tk.Frame(history_box, bg="#2ecc71")
        history_inner.pack(padx=6, pady=6, fill="x")
        nota_logo = tk.Label(history_inner, text="🧾", font=("Segoe UI Emoji", 14), bg="#2ecc71", fg="white")
        nota_logo.pack(side="left", padx=(0, 6))
        btn5 = tk.Button(
            history_inner, text="History", command=self.show_history,
            bg="#2ecc71", fg="white", activebackground="#27ae60", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn5.pack(side="left", fill="x", expand=True)
        logout_box = tk.Frame(opsi_frame, bg="#e74c3c", bd=2, relief="groove")
        logout_box.pack(pady=6, fill="x")
        logout_inner = tk.Frame(logout_box, bg="#e74c3c")
        logout_inner.pack(padx=6, pady=6, fill="x")
        x_logo = tk.Label(logout_inner, text="❌", font=("Segoe UI Emoji", 14), bg="#e74c3c", fg="white")
        x_logo.pack(side="left", padx=(0, 6))
        btn6 = tk.Button(
            logout_inner, text="Logout", command=self.show_role_menu,
            bg="#e74c3c", fg="white", activebackground="#c0392b", activeforeground="white",
            borderwidth=0, font=STYLE["font_normal"], width=22, pady=2
        )
        btn6.pack(side="left", fill="x", expand=True)


    def menu_cari_produk(self):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title("Pilih Kategori Produk")
        label = tk.Label(win, text="Pilih Kategori:")
        apply_label_style(label)
        label.pack(pady=10)
        def show_kat(kat):
            win.destroy()
            self.show_produk_by_kategori(kat)
        btn1 = tk.Button(win, text="Others/Miscellaneous", command=lambda: show_kat("Miscellaneous"))
        apply_button_style(btn1, "primary")
        btn1.pack(pady=STYLE["pad_y"])
        btn2 = tk.Button(win, text="Elektronik", command=lambda: show_kat("Elektronik"))
        apply_button_style(btn2, "success")
        btn2.pack(pady=STYLE["pad_y"])
        btn3 = tk.Button(win, text="Pakaian", command=lambda: show_kat("Pakaian"))
        apply_button_style(btn3, "default")
        btn3.pack(pady=STYLE["pad_y"])
        btn4 = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn4, "danger")
        btn4.pack(pady=STYLE["pad_y"])


    def show_produk_by_kategori(self, kategori):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title(f"Produk {kategori}")
        produk_list = self.sistem.get_products_by_category(kategori)
        listbox = Listbox(win, width=80)
        listbox.pack(pady=10)
        for p in produk_list:
            penjual = self.sistem.get_penjual_by_email(p.get_penjual_email())
            nama_toko = penjual.get_nama_toko() if penjual else "-"
            listbox.insert(END, f"{p.get_nama()} | Toko: {nama_toko} | Stok: {p.get_stok()} | Rp{p.get_harga():,}")
        def detail():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Produk", "Pilih produk untuk detail!", parent=win)
                return
            produk = produk_list[idx[0]]
            penjual = self.sistem.get_penjual_by_email(produk.get_penjual_email())
            nama_toko = penjual.get_nama_toko() if penjual else "-"
            detail = produk.show_info() + f"\nToko: {nama_toko}" #polymorphism
            aksi_win = Toplevel(win, bg=STYLE["bg_main"])
            aksi_win.title("Aksi Produk")
            label = tk.Label(aksi_win, text=detail, justify="left")
            apply_label_style(label)
            label.pack(pady=10)
            def tambah_keranjang():
                jumlah = simpledialog.askinteger("Jumlah", "Masukkan jumlah ke keranjang:", minvalue=1, maxvalue=produk.get_stok(), parent=aksi_win)
                if jumlah:
                    user = self.sistem.get_current_user()
                    user.tambah_ke_keranjang(produk, jumlah)
                    messagebox.showinfo("Sukses", "Produk ditambahkan ke keranjang!", parent=aksi_win)
                aksi_win.destroy()
            def beli_sekarang():
                jumlah = simpledialog.askinteger("Jumlah", "Masukkan jumlah yang ingin dibeli:", minvalue=1, maxvalue=produk.get_stok(), parent=aksi_win)
                if jumlah:
                    self.pilih_metode_pembayaran_gui(produk, jumlah, aksi_win)
            btn1 = tk.Button(aksi_win, text="Tambah ke Keranjang", command=tambah_keranjang)
            apply_button_style(btn1, "primary")
            btn1.pack(pady=STYLE["pad_y"])
            btn2 = tk.Button(aksi_win, text="Beli Sekarang", command=beli_sekarang)
            apply_button_style(btn2, "success")
            btn2.pack(pady=STYLE["pad_y"])
            btn3 = tk.Button(aksi_win, text="Tutup", command=aksi_win.destroy)
            apply_button_style(btn3, "danger")
            btn3.pack(pady=STYLE["pad_y"])
        btn = tk.Button(win, text="Detail Produk", command=detail)
        apply_button_style(btn, "primary")
        btn.pack(pady=STYLE["pad_y"])
        btn2 = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn2, "danger")
        btn2.pack(pady=STYLE["pad_y"])


    def menu_cari_toko(self):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title("Daftar Toko")
        penjual_list = self.sistem.get_sellers()
        listbox = Listbox(win, width=60)
        listbox.pack(pady=10)
        for p in penjual_list:
            listbox.insert(END, f"{p.get_nama_toko()} | Alamat: {p.get_alamat()}")
        def pilih_toko():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Toko", "Pilih toko!", parent=win)
                return
            penjual = penjual_list[idx[0]]
            win.destroy()
            self.menu_kategori_toko(penjual)
        btn1 = tk.Button(win, text="Pilih Toko", command=pilih_toko)
        apply_button_style(btn1, "primary")
        btn1.pack(pady=STYLE["pad_y"])
        btn2 = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn2, "danger")
        btn2.pack(pady=STYLE["pad_y"])


    def menu_kategori_toko(self, penjual):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title(f"Kategori di {penjual.get_nama_toko()}")
        label = tk.Label(win, text="Pilih Kategori:")
        apply_label_style(label)
        label.pack(pady=10)
        def show_kat(kat):
            win.destroy()
            self.show_produk_toko_by_kategori(penjual, kat)
        btn1 = tk.Button(win, text="Others/Miscellaneous", command=lambda: show_kat("Miscellaneous"))
        apply_button_style(btn1, "primary")
        btn1.pack(pady=STYLE["pad_y"])
        btn2 = tk.Button(win, text="Elektronik", command=lambda: show_kat("Elektronik"))
        apply_button_style(btn2, "success")
        btn2.pack(pady=STYLE["pad_y"])
        btn3 = tk.Button(win, text="Pakaian", command=lambda: show_kat("Pakaian"))
        apply_button_style(btn3, "default")
        btn3.pack(pady=STYLE["pad_y"])
        btn4 = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn4, "danger")
        btn4.pack(pady=STYLE["pad_y"])


    def show_produk_toko_by_kategori(self, penjual, kategori):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title(f"Produk {kategori} di {penjual.get_nama_toko()}")
        produk_list = [p for p in self.sistem.get_products_by_seller(penjual.get_email()) if p.get_kategori() == kategori]
        listbox = Listbox(win, width=80)
        listbox.pack(pady=10)
        for p in produk_list:
            listbox.insert(END, f"{p.get_nama()} | Stok: {p.get_stok()} | Rp{p.get_harga():,}")
        def detail():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Produk", "Pilih produk untuk detail!", parent=win)
                return
            produk = produk_list[idx[0]]
            penjual = self.sistem.get_penjual_by_email(produk.get_penjual_email())
            nama_toko = penjual.get_nama_toko() if penjual else "-"
            detail = produk.show_info() + f"\nToko: {nama_toko}"
            aksi_win = Toplevel(win, bg=STYLE["bg_main"])
            aksi_win.title("Aksi Produk")
            label = tk.Label(aksi_win, text=detail, justify="left")
            apply_label_style(label)
            label.pack(pady=10)
            def tambah_keranjang():
                jumlah = simpledialog.askinteger("Jumlah", "Masukkan jumlah ke keranjang:", minvalue=1, maxvalue=produk.get_stok(), parent=aksi_win)
                if jumlah:
                    user = self.sistem.get_current_user()
                    user.tambah_ke_keranjang(produk, jumlah)
                    messagebox.showinfo("Sukses", "Produk ditambahkan ke keranjang!", parent=aksi_win)
                aksi_win.destroy()
            def beli_sekarang():
                jumlah = simpledialog.askinteger("Jumlah", "Masukkan jumlah yang ingin dibeli:", minvalue=1, maxvalue=produk.get_stok(), parent=aksi_win)
                if jumlah:
                    self.pilih_metode_pembayaran_gui(produk, jumlah, aksi_win)
            btn1 = tk.Button(aksi_win, text="Tambah ke Keranjang", command=tambah_keranjang)
            apply_button_style(btn1, "primary")
            btn1.pack(pady=STYLE["pad_y"])
            btn2 = tk.Button(aksi_win, text="Beli Sekarang", command=beli_sekarang)
            apply_button_style(btn2, "success")
            btn2.pack(pady=STYLE["pad_y"])
            btn3 = tk.Button(aksi_win, text="Tutup", command=aksi_win.destroy)
            apply_button_style(btn3, "danger")
            btn3.pack(pady=STYLE["pad_y"])
        btn = tk.Button(win, text="Detail Produk", command=detail)
        apply_button_style(btn, "primary")
        btn.pack(pady=STYLE["pad_y"])
        btn2 = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn2, "danger")
        btn2.pack(pady=STYLE["pad_y"])


    def show_keranjang(self):
        keranjang = self.sistem.get_current_user().get_keranjang()
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title("Keranjang Belanja")
        label = tk.Label(win, text="Keranjang Anda:")
        apply_label_style(label)
        label.pack(pady=10)
        listbox = Listbox(win, width=80)
        listbox.pack(pady=10)
        produk_list = []
        total = 0
        for item in keranjang:
            produk = item["produk"]
            jumlah = item["jumlah"]
            subtotal = produk.get_harga() * jumlah
            penjual = self.sistem.get_penjual_by_email(produk.get_penjual_email())
            nama_toko = penjual.get_nama_toko() if penjual else "-"
            listbox.insert(END, f"{produk.get_nama()} | Toko: {nama_toko} | Jumlah: {jumlah} | Harga: Rp{produk.get_harga():,} | Subtotal: Rp{subtotal:,}")
            produk_list.append((produk, jumlah))
            total += subtotal
        total_label = tk.Label(win, text=f"Total: Rp{total:,}")
        apply_label_style(total_label)
        total_label.pack(pady=5)
        def hapus_item():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Item", "Pilih item yang akan dihapus!", parent=win)
                return
            produk, jumlah_di_keranjang = produk_list[idx[0]]
            jumlah_hapus = simpledialog.askinteger(
                "Hapus Produk", f"Masukkan jumlah yang ingin dihapus (maksimal {jumlah_di_keranjang}):",
                minvalue=1, maxvalue=jumlah_di_keranjang, parent=win)
            if jumlah_hapus is None:
                return
            user = self.sistem.get_current_user()
            for item in user.get_keranjang():
                if item["produk"].get_id_produk() == produk.get_id_produk():
                    if jumlah_hapus >= item["jumlah"]:
                        user.hapus_dari_keranjang(produk.get_id_produk())
                    else:
                        item["jumlah"] -= jumlah_hapus
                    break
            win.destroy()
            self.show_keranjang()
        def checkout():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Item", "Pilih produk yang ingin di-checkout!", parent=win)
                return
            produk, jumlah_di_keranjang = produk_list[idx[0]]
            stok_tersedia = produk.get_stok()
            max_checkout = min(jumlah_di_keranjang, stok_tersedia)
            if max_checkout == 0:
                messagebox.showwarning("Stok Habis", "Stok produk ini sudah habis!", parent=win)
                return
            jumlah_checkout = simpledialog.askinteger(
                "Checkout", f"{produk.get_nama()} (Stok: {stok_tersedia}, Di Keranjang: {jumlah_di_keranjang})\nMasukkan jumlah checkout:",
                minvalue=1, maxvalue=max_checkout, parent=win)
            if jumlah_checkout:
                self.pilih_metode_pembayaran_gui_keranjang(produk, jumlah_checkout, keranjang, win)
        btn_hapus = tk.Button(win, text="Hapus Item", command=hapus_item)
        apply_button_style(btn_hapus, "danger")
        btn_hapus.pack(pady=STYLE["pad_y"])
        btn_checkout = tk.Button(win, text="Checkout", command=checkout)
        apply_button_style(btn_checkout, "primary")
        btn_checkout.pack(pady=STYLE["pad_y"])
        btn_tutup = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn_tutup, "default")
        btn_tutup.pack(pady=STYLE["pad_y"])


    def pilih_metode_pembayaran_gui(self, produk, jumlah, parent):
        win = Toplevel(parent)
        win.title("Pilih Metode Pembayaran")
        tk.Label(win, text="Pilih Metode Pembayaran:", font=("Arial", 12, "bold")).pack(pady=10)
        def bayar(metode):
            sukses, msg = self.sistem.buat_pesanan(produk, jumlah, metode)
            if sukses:
                messagebox.showinfo("Pembelian", msg, parent=win)
            else:
                messagebox.showerror("Pembelian", msg, parent=win)
            win.destroy()
            parent.destroy()
        tk.Button(win, text="GoPay", width=20, command=lambda: bayar("GoPay")).pack(pady=5)
        tk.Button(win, text="Dana", width=20, command=lambda: bayar("Dana")).pack(pady=5)
        tk.Button(win, text="Bank", width=20, command=lambda: bayar("Bank")).pack(pady=5)
        tk.Button(win, text="OVO", width=20, command=lambda: bayar("OVO")).pack(pady=5)
        tk.Button(win, text="Batal", width=20, command=win.destroy).pack(pady=5)


    def pilih_metode_pembayaran_gui_keranjang(self, produk, jumlah, keranjang, parent):
        win = Toplevel(parent)
        win.title("Pilih Metode Pembayaran")
        tk.Label(win, text="Pilih Metode Pembayaran:", font=("Arial", 12, "bold")).pack(pady=10)
        def bayar(metode):
            sukses, msg = self.sistem.buat_pesanan(produk, jumlah, metode)
            if sukses:
                for item in keranjang:
                    if item["produk"].get_id_produk() == produk.get_id_produk():
                        if jumlah == item["jumlah"]:
                            keranjang.remove(item)
                        else:
                            item["jumlah"] -= jumlah
                        break
                messagebox.showinfo("Pembelian", msg, parent=win)
            else:
                messagebox.showerror("Pembelian", msg, parent=win)
            win.destroy()
            parent.destroy()
            self.show_keranjang()
        tk.Button(win, text="GoPay", width=20, command=lambda: bayar("GoPay")).pack(pady=5)
        tk.Button(win, text="Dana", width=20, command=lambda: bayar("Dana")).pack(pady=5)
        tk.Button(win, text="Bank", width=20, command=lambda: bayar("Bank")).pack(pady=5)
        tk.Button(win, text="OVO", width=20, command=lambda: bayar("OVO")).pack(pady=5)
        tk.Button(win, text="Batal", width=20, command=win.destroy).pack(pady=5)


    def show_daftar_pesanan(self):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title("Daftar Pesanan")
        label = tk.Label(win, text="Daftar Pesanan Anda:")
        apply_label_style(label)
        label.pack(pady=10)
        produk_tersedia = {p.get_id_produk() for p in self.sistem.get_products()}
        pesanan_saya = [
            p for p in self.sistem.get_pesanan()
            if (
                p.get_pembeli_email() == self.sistem.get_current_user().get_email()
                and p.get_status() in ("Pending", "Dikirim")
            )
        ]
        for p in pesanan_saya:
            if p.get_produk().get_id_produk() not in produk_tersedia and p.get_status() == "Pending":
                p.set_status("Dibatalkan")
        listbox = Listbox(win, width=100)
        listbox.pack(pady=10)
        for p in pesanan_saya:
            produk = p.get_produk()
            penjual = self.sistem.get_penjual_by_email(produk.get_penjual_email())
            nama_toko = penjual.get_nama_toko() if penjual else "-"
            listbox.insert(END, f"{produk.get_nama()} | Toko: {nama_toko} | Jumlah: {p.get_jumlah()} | Total: Rp{p.get_total_harga():,} | Status: {p.get_status()} | Metode: {p.get_metode_pembayaran()}")
        def aksi():
            idx = listbox.curselection()
            if not idx:
                messagebox.showwarning("Pilih Pesanan", "Pilih pesanan!", parent=win)
                return
            pesanan = pesanan_saya[idx[0]]
            aksi_win = Toplevel(win, bg=STYLE["bg_main"])
            aksi_win.title("Konfirmasi Pesanan")
            label = tk.Label(aksi_win, text=f"Pesanan: {pesanan.get_produk().get_nama()}\nJumlah: {pesanan.get_jumlah()}\nStatus: {pesanan.get_status()}")
            apply_label_style(label)
            label.pack(pady=10)
            if pesanan.get_status() == "Dikirim":
                def konfirmasi():
                    pesanan.set_status("Selesai")
                    messagebox.showinfo("Pesanan", "Pesanan diterima! Masuk ke history.", parent=aksi_win)
                    aksi_win.destroy()
                    win.destroy()
                    self.show_daftar_pesanan()
                btn_konf = tk.Button(aksi_win, text="Konfirmasi Diterima", command=konfirmasi)
                apply_button_style(btn_konf, "success")
                btn_konf.pack(pady=STYLE["pad_y"])
            btn_tutup = tk.Button(aksi_win, text="Tutup", command=aksi_win.destroy)
            apply_button_style(btn_tutup, "default")
            btn_tutup.pack(pady=STYLE["pad_y"])
        btn_aksi = tk.Button(win, text="Konfirmasi Pesanan", command=aksi)
        apply_button_style(btn_aksi, "primary")
        btn_aksi.pack(pady=STYLE["pad_y"])
        btn_tutup = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn_tutup, "default")
        btn_tutup.pack(pady=STYLE["pad_y"])


    def show_history(self):
        win = Toplevel(self.root, bg=STYLE["bg_main"])
        win.title("History Pesanan")
        label = tk.Label(win, text="History Pesanan Anda:")
        apply_label_style(label)
        label.pack(pady=10)
        pesanan_saya = [p for p in self.sistem.get_pesanan() if p.get_pembeli_email() == self.sistem.get_current_user().get_email()]
        listbox = Listbox(win, width=100)
        listbox.pack(pady=10)
        for p in pesanan_saya:
            produk = p.get_produk()
            penjual = self.sistem.get_penjual_by_email(produk.get_penjual_email())
            nama_toko = penjual.get_nama_toko() if penjual else "-"
            listbox.insert(END, f"{produk.get_nama()} | Toko: {nama_toko} | Jumlah: {p.get_jumlah()} | Total: Rp{p.get_total_harga():,} | Status: {p.get_status()} | Metode: {p.get_metode_pembayaran()}")
        btn_tutup = tk.Button(win, text="Tutup", command=win.destroy)
        apply_button_style(btn_tutup, "default")
        btn_tutup.pack(pady=STYLE["pad_y"])







if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x600")
    app = App(root)
    root.mainloop()