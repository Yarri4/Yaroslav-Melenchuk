# 2023/11/05 00:00|Дополнительное практическое задание по модулю*
# Дополнительное практическое задание по модулю: "Классы и объекты."


import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хэшируем пароль
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f'Пользователь {nickname} вошел в систему.')
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован и автоматически вошел в систему.')

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f'Видео "{video.title}" добавлено.')
            else:
                print(f'Видео "{video.title}" уже существует.')

    def get_videos(self, keyword):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        
        for video in self.videos:
            if video.title == title:
                if self.current_user.age < 18 and video.adult_mode:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                
                print(f'Начинаем просмотр видео "{title}".')
                while video.time_now < video.duration:
                    print(f'Секунда {video.time_now + 0.5}...')
                    video.time_now += 1
                    time.sleep(0.5)  # Пауза в 0.5 секунд
                print("Конец видео")
                video.time_now = 0  # Сброс времени просмотра
                return
        
        print("Видео не найдено.")

# Пример использования классов
if __name__ == "__main__":
    ur = UrTube()
    
    # Регистрация пользователей
    ur.register("user1", "password123", 25)
    ur.register("user2", "password456", 17)

    # Добавление видео
    video1 = Video("Urban the best", 10, adult_mode=True)
    video2 = Video("Nature documentary", 5)
    ur.add(video1, video2)

    # Вход в систему
    ur.log_in("user1", "password123")
    
    # Просмотр видео
    ur.watch_video("Urban the best")
    
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
    
    # Выход из системы
    ur.log_out()
    
