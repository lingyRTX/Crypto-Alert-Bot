"""Скрипт для создания EXE файла с PyInstaller"""
import os
import shutil
import subprocess
import sys
import io

# Фиксим кодировку для эмодзи на Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def build_exe():
    """Собрать EXE файл"""
    print("🔨 Начинаем сборку CryptoAlertBot...")

    # Удалить старый EXE если он существует
    old_exe = "dist/CryptoAlertBot.exe"
    if os.path.exists(old_exe):
        try:
            os.remove(old_exe)
        except:
            # Если не удалось удалить, переименуем
            try:
                os.rename(old_exe, "dist/CryptoAlertBot.exe.old")
            except:
                pass

    # Параметры PyInstaller
    pyinstaller_args = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # Один EXE файл
        "--windowed",  # Без консоли
        "--name=CryptoAlertBot",  # Имя приложения
        "--distpath=dist",  # Папка для EXE
        "--workpath=build",  # Папка сборки
        "--specpath=.",  # Папка для .spec файла
        "main.py"
    ]

    # Запустить PyInstaller
    try:
        result = subprocess.run(pyinstaller_args, check=False)
        if result.returncode == 0:
            print("\n✅ Сборка успешна!")
            print("📦 EXE файл находится в папке: dist/CryptoAlertBot.exe")

            # Скопировать config.json в dist
            if os.path.exists("config.json"):
                shutil.copy("config.json", "dist/config.json")
                print("📋 config.json скопирован в dist/")

            print("\n🚀 Вы можете запустить: dist/CryptoAlertBot.exe")
        else:
            print("\n❌ Ошибка при сборке")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build_exe()
