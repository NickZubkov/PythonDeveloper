import time


class User:

    def __init__(self, name, password, age=None):
        self.name = name
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.password == other.password

    def __str__(self):
        return self.name

class Video:

    def __init__(self, title, duration, adult_mode=None):
        self.title = title
        self.duration = duration
        self.time_now = 0
        if adult_mode is None:
            self.adult_mode = False
        else:
            self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        tmp_user = User(nickname, password)
        for user in self.users:
            if user == tmp_user:
                self.current_user = user
                print(f"Выполнен вход для пользователя {self.current_user.name}")
                return
        print("Не верное имя пользователя или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.name == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f"Зарегистрирован пользователь {new_user.name}")
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add(self, *videos):
        for video in videos:
            if isinstance(video, Video):
                if any(v.title == video.title for v in self.videos):
                    print(f"Видео с названием '{video.title}' уже существует")
                else:
                    self.videos.append(video)

    def get_videos(self, searching_word):
        selected_videos = []
        for video in self.videos:
            if str.lower(video.title).__contains__(str.lower(searching_word)):
                selected_videos.append(video.title)
        if selected_videos.__len__() <= 0:
            print("Совпадений не найдено")
        else:
            return selected_videos

    def watch_video(self, video_name):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        selected_video = None
        for video in self.videos:
            if video.title == video_name:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                else:
                    selected_video = video
                break

        if selected_video is None:
            print(f"Видео c именем '{video_name}' не найдено")
            return

        while selected_video.time_now < selected_video.duration:
            time.sleep(1)
            selected_video.time_now += 1
            print(selected_video.time_now)
        selected_video.time_now = 0
        print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v4 = Video('Для чего девушкам парень?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v3, v4)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('го'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.log_in("vasya_pupkin", "lolkekcheburek")
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Выход из аккаунта
ur.log_out()
print(ur.current_user)





