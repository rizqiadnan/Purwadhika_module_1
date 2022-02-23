# import modules
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


reportSiswa = {
    '12A': {
        'Nama': 'Muhammad Rizqi Adnan Pratama',
        'Gender': 'Laki-Laki',
        'Umur': 22,
        'Kota': 'Jakarta'
    },
    '12B': {
        'Nama': 'Rizqillah Zahra Lestari',
        'Gender': 'Perempuan',
        'Umur': 21,
        'Kota': 'Bekasi'
    },
}


def showAllData():
    for siswaID, siswaInfo in reportSiswa.items():
        print("\n" + "No. " + siswaID)
        for key in siswaInfo:
            print(key + ':', siswaInfo[key])


def main_menu():
    print("========= Data Record =========")
    print("1. Report Data Siswa")
    print("2. Add Data Siswa")
    print("3. Update Data Siswa")
    print("4. Delete Data Siswa")
    print("5. Exit")
    selected_menu = int(input("Silakan Pilih Main_Menu [1-5] : "))

    if (selected_menu == 1):
        clear_screen()
        menu_read()
    elif (selected_menu == 2):
        clear_screen()
        menu_add()
    elif (selected_menu == 3):
        clear_screen()
        menu_update()
    elif (selected_menu == 4):
        clear_screen()
        menu_delete()
    elif (selected_menu == 5):
        print("Thank you and Good Bye!!!")
    else:
        clear_screen()
        print("********* Pilihan yang anda masukkan Salah *********")
        main_menu()


def menu_read():
    print("+++++ Report Data Siswa +++++")
    print("1. Report Seluruh Data")
    print("2. Report Data Tertentu")
    print("3. Kembali Ke Menu Utama")
    selected_menu_read = int(
        input("Silakan Pilih Sub Menu Read Data [1-3] : "))
    if (selected_menu_read == 1):
        showAllData()
        menu_read()
    elif (selected_menu_read == 2):
        selected_nim = input("Masukkan NIM : ")
        print("Data Siswa dengan NIM : ", selected_nim)
        if selected_nim in reportSiswa.keys():
            print(reportSiswa[selected_nim])
        else:
            print("******Tidak ada data pada report siswa****** \n")
        menu_read()
    elif (selected_menu_read == 3):
        main_menu()
    else:
        menu_read()


def menu_add():
    print("+++++ Add Data Siswa +++++")
    print("1. Tambah Data Siswa")
    print("2. Kembali Ke Menu Utama")
    selected_menu_add = int(
        input("Silakan Pilih Sub Menu Create Data [1-2] : "))

    if (selected_menu_add == 1):
        added_nim = input("Masukkan NIM : ")
        if added_nim in reportSiswa.keys():
            print("Data Siswa dengan NIM : ", added_nim, "sudah ada")
            menu_add()
        else:
            added_name = input("Masukkan Nama : ")
            added_gender = input("Masukkan Gender : ")
            added_city = input("Masukkan Kota : ")
            added_age = input("Masukkan Umur : ")

            confirmation_option = input("Apakah Data akan disimpan? (Y/N) : ")
            while ((confirmation_option != 'Y') & (confirmation_option != 'N')):
                confirmation_option_2 = input(
                    "Apakah Data akan disimpan? (Y/N) : ")
                confirmation_option = confirmation_option_2

            if (confirmation_option == 'Y'):
                reportSiswa[added_nim] = {
                    'Nama': added_name,
                    'Gender': added_gender,
                    'Kota': added_city,
                    'Umur': added_age
                }
                print("Data Tersimpan")
                showAllData()
                menu_add()
            elif (confirmation_option == 'N'):
                print("Data tidak tersimpan")
                menu_add()
            else:
                confirmation_option_3 = input(
                    "Apakah Data akan disimpan? (Y/N) : ")
                confirmation_option = confirmation_option_3
    elif (selected_menu_add == 2):
        main_menu()
    else:
        main_menu()


def menu_update():
    print("+++++ Update Data Siswa +++++")
    print("1. Ubah Data Siswa")
    print("2. Kembali Ke Menu Utama")

    selected_menu_update = int(
        input("Silakan Pilih Sub Menu Update Data [1-2] : "))

    if (selected_menu_update == 1):
        updated_nim = input("Masukkan NIM : ")

        if updated_nim in reportSiswa.keys():
            print(reportSiswa[updated_nim])
            confirmation_update_option = input(
                "Tekan Y jika ingin lanjut update data atau N jika ingin cancel (Y/N) : ")
            while ((confirmation_update_option != 'Y') & (confirmation_update_option != 'N')):
                confirmation_update_option_2 = input(
                    "Tekan Y jika ingin lanjut update data atau N jika ingin cancel (Y/N) : ")
                confirmation_update_option = confirmation_update_option_2

            if (confirmation_update_option == 'Y'):
                selected_column_updated = input(
                    "Masukkan nama kolom/keterangan yang ingin di update (Nama/Gender/Kota/Umur): ")
                updated_value = input(
                    "Masukkan {} Baru : ".format(selected_column_updated))
                confirmation_update = input(
                    "Apakah data ingin di update? (Y/N) : ")
                while ((confirmation_update != 'Y') & (confirmation_update != 'N')):
                    confirmation_update_2 = input(
                        "Apakah data ingin di update? (Y/N) : ")
                    confirmation_update = confirmation_update_2

                if (confirmation_update == 'Y'):
                    reportSiswa[updated_nim][selected_column_updated] = updated_value
                    print("Data updated")
                    showAllData()
                elif (confirmation_update == 'N'):
                    print("Data tidak terupdate")
                    menu_update()
                else:
                    confirmation_update_3 = input(
                        "Apakah data ingin di update? (Y/N) : ")
                    confirmation_update = confirmation_update_3
            elif (confirmation_update_option == 'N'):
                print("Data tidak terupdate")
                menu_update()
            else:
                confirmation_update_option_2 = input(
                    "Tekan Y jika ingin lanjut update data atau N jika ingin cancel (Y/N) : ")
                confirmation_update_option = confirmation_update_option_2
            menu_update()
        else:
            print("Data tidak ada")
            menu_update()

    elif (selected_menu_update == 2):
        main_menu()
    else:
        menu_update()


def menu_delete():
    print("+++++ Delete Data Siswa +++++")
    print("1. Delete Data Siswa")
    print("2. Kembali Ke Menu Utama")
    selected_menu_delete = int(
        input("Silakan Pilih Sub Menu Delete Data [1-2] : "))
    if (selected_menu_delete == 1):
        deleted_nim = input("Masukkan NIM : ")

        if deleted_nim in reportSiswa.keys():
            confirmation_delete_option = input(
                "Apakah Data akan dihapus (Y/N) : ")
            while ((confirmation_delete_option != 'Y') & (confirmation_delete_option != 'N')):
                confirmation_delete_option_2 = input(
                    "Apakah Data akan dihapus (Y/N) : ")
                confirmation_delete_option = confirmation_delete_option_2

            if (confirmation_delete_option == 'Y'):
                del reportSiswa[deleted_nim]
                print("Data deleted")
                showAllData()
            elif (confirmation_delete_option == 'N'):
                print("Data tidak terhapus")
                menu_delete()
            else:
                confirmation_delete_option_3 = input(
                    "Apakah Data akan dihapus (Y/N) : ")
                confirmation_delete_option = confirmation_delete_option_3
        else:
            print("Data tidak ada")
        menu_delete()
    elif (selected_menu_delete == 2):
        main_menu()
    else:
        menu_delete()


main_menu()
