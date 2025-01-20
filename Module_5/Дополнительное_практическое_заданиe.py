import time

class User:
    nickname: str
    password: int
    age: int
    
    def __init__(self, nickname: str, password: str, age: int) -> None:
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

        
    def passwd_check(self, password: str) -> bool:
        return hash(password) == self.password

    def __str__(self) -> str:
        return self.nickname


class Video:
    title: str
    duration: int
    time_now: int = 0
    adult_mode: bool

    def __init__(self, title: str, duration: int, adult_mode: bool = False) -> None:
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __repr__(self) -> str:
        return self.title

class UrTube:
    users: list[User] = []
    videos: list[Video] = []
    current_user: User | None = None
    
    def find_user(self, nickname: str) -> User | None:
        for user in self.users:
            if user.nickname == nickname:
                return user
        return

    
    def log_in(self, nickname: str, password: str, user: User | None = None) -> bool:
        if not user:
            user = self.find_user(nickname)
        if user:
            if user.passwd_check(password):
                self.current_user = user
                return True
            print('Введен неверный пароль!')
            return False
        print("Пользователь не найден!")
        return False

    def register(self, nickname: str, password: str, age: int) -> bool:
        user_exists = self.find_user(nickname)
        if user_exists:
            print(f"Пользователь {nickname} уже существует")
            return False
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password, new_user)
        return True
     
    def log_out(self):
        self.current_user = None
        print("Пользователь вышел из системы")

    def add(self, *videos: Video) -> None:
        for video in videos:
            self.videos.append(video)

    def get_videos(self, prompt: str) -> list:
        videos_found: list = []
        for video in self.videos:
            if prompt.casefold() in video.title.casefold():
                videos_found.append(video)
        return videos_found
    
    def play_video(self, video: Video) -> None:
        for i in range(1, video.duration):
            print(i, end=' ')
            time.sleep(1)
            video.duration += 1
        video.duration = 0
        print('Конец видео')

    def validate_user(self, video: Video) -> int:
        if not self.current_user:
            return 2
        if video.adult_mode:
            return self.current_user.age >= 18
        return 1
    
    def watch_video(self, exact_name: str) -> None:
        for video in self.videos:
            if video.title == exact_name:
                is_valid_user = self.validate_user(video)
                if is_valid_user == 1:
                    self.play_video(video)
                    return
                elif is_valid_user == 0:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                print('Войдите в аккаунт, чтобы смотреть видео')
                


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



                


                




