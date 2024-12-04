import os

class PhongHoc:
    def __init__(self, maPhong, dayNha, dienTich, soBongDen):
        self.maPhong = maPhong
        self.dayNha = dayNha
        self.dienTich = dienTich
        self.soBongDen = soBongDen
    def check(self):
        return self.dienTich / 10 <= float(self.soBongDen)
    def describe(self):
        return f"Mã phòng: {self.maPhong}\nDãy nhà: {self.dayNha}\nDiện tích: {self.dienTich}\nSố bóng đèn: {self.soBongDen}"

class PhongHocLyThuyet(PhongHoc):
    def __init__(self, maPhong, dayNha, dienTich, soBongDen, mayChieu):
        super().__init__(maPhong, dayNha, dienTich, soBongDen)
        self.mayChieu = mayChieu
    def check(self):
        return super().check() and self.mayChieu
    def describe(self):
        return super().describe() + f"\n{'Có' if self.mayChieu else 'Không có'} máy chiếu"

class PhongMayTinh(PhongHoc):
    def __init__(self, maPhong, dayNha, dienTich, soBongDen, soLuongMayTinh):
        super().__init__(maPhong, dayNha, dienTich, soBongDen)
        self.soLuongMayTinh = soLuongMayTinh
    def check(self):
        return super().check() and self.dienTich / self.soLuongMayTinh >= 1.5
    def describe(self):
        return super().describe() + f"\nSố lượng máy tính: {self.soLuongMayTinh}"

class QuanLyPhongHoc:
    def __init__(self):
        self.danhSachPhong = []

    def ThemPhongHoc(self, phong):
        for p in self.danhSachPhong:
            if p.maPhong == phong.maPhong:
                print("Phòng đã tồn tại!")
                return
        else:
            self.danhSachPhong.append(phong)

    def TimKiemPhongHoc(self, maPhong):
        for p in self.danhSachPhong:
            if p.maPhong == maPhong:
                return p
        return None

    def ToanBoPhongHoc(self):
        for p in self.danhSachPhong:
            print(p.describe())

    def PhongHocDatChuan(self):
        for p in self.danhSachPhong:
            if p.check():
                print(p.describe())

    def CapNhatSoLuongMayTinh(self, maPhong, soLuongMayMoi):
        phong = self.TimKiemPhongHoc(maPhong)
        if phong and isinstance(phong, PhongMayTinh):
            phong.soLuongMayTinh += soLuongMayMoi
        else:
            print("Không tìm thấy phòng máy tính hoặc mã phòng không hợp lệ!")

    def XoaPhongHoc(self, maPhong):
        phong = self.TimKiemPhongHoc(maPhong)
        if phong:
            confirm = input(f"Bạn có chắc chắn muốn xóa phòng {maPhong} không (Yes/No): ")
            if confirm.lower() in ['yes', 'y']:
                self.danhSachPhong.remove(phong)
                print(f"Đã xóa phòng {maPhong}.")
            else:
                print("Hủy xóa phòng.")
        else:
            print("Không tìm thấy phòng cần xóa.")

    def SoLuongPhongHoc(self):
        return len(self.danhSachPhong)

    def PhongHoc60May(self):
        for p in self.danhSachPhong:
            if isinstance(p, PhongMayTinh) and p.soLuongMayTinh == 60:
                print(p.describe())

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    manager = QuanLyPhongHoc()

    while True:
        clear_screen()
        print("\n=== QUẢN LÝ PHÒNG HỌC ===")
        print("1. Thêm phòng học")
        print("2. Tìm kiếm phòng học")
        print("3. Lấy thông tin toàn bộ danh sách các phòng học")
        print("4. Lấy thông tin danh sách các phòng học đạt chuẩn")
        print("5. Cập nhật số lượng máy tính cho phòng học máy tính")
        print("6. Xóa phòng học")
        print("7. Tính tổng số lượng phòng học")
        print("8. Lấy thông tin danh sách các phòng học máy tính có 60 máy")
        print("0. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            maPhong = input("Nhập mã phòng: ")
            dayNha = input("Nhập dãy nhà: ")
            dienTich = float(input("Nhập diện tích phòng: "))
            soBongDen = int(input("Số bóng đèn: "))

            loaiPhong = input("Chọn loại phòng (1. Lý thuyết / 2. Máy tính): ")

            if loaiPhong == "1":
                mayChieu = input("Có máy chiếu không? (Yes/No): ").strip().lower() in ['yes', 'y']
                phong = PhongHocLyThuyet(maPhong, dayNha, dienTich, soBongDen, mayChieu)
                manager.ThemPhongHoc(phong)

            elif loaiPhong == "2":
                soLuongMayTinh = int(input("Nhập số lượng máy tính: "))
                phong = PhongMayTinh(maPhong, dayNha, dienTich, soBongDen, soLuongMayTinh)
                manager.ThemPhongHoc(phong)

            else:
                print("Loại phòng không hợp lệ!")

        elif choice == '2':
            maPhong = input("Nhập mã phòng cần tìm: ")
            phong = manager.TimKiemPhongHoc(maPhong)
            if phong:
                print(phong.describe())
            else:
                print("Không tìm thấy phòng.")

        elif choice == '3':
            manager.ToanBoPhongHoc()

        elif choice == '4':
            manager.PhongHocDatChuan()

        elif choice == '5':
            maPhong = input("Nhập mã phòng cần cập nhật số lượng máy tính: ")
            soLuongMayMoi = int(input("Nhập số lượng máy tính mới: "))
            manager.CapNhatSoLuongMayTinh(maPhong, soLuongMayMoi)

        elif choice == '6':
            maPhong = input("Nhập mã phòng cần xóa: ")
            manager.XoaPhongHoc(maPhong)

        elif choice == '7':
            print(f"Tổng số lượng phòng học: {manager.SoLuongPhongHoc()}")

        elif choice == '8':
            manager.PhongHoc60May()

        elif choice == '0':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")

        input("Nhấn Enter để tiếp tục...")

if __name__ == "__main__":
    menu()