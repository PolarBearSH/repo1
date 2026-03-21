'''
14. Турнир по шахматам

- Реализуйте систему турнира между игроками.

- Создайте класс Player, который содержит:
  -- имя;
  -- рейтинг;
  -- количество побед;
  -- количество поражений;
  -- количество ничьих;
  -- количество очков.

- Создайте класс Match, который содержит:
  -- двух игроков;
  -- результат матча;
  -- дату;
  -- длительность партии.

- Создайте класс Tournament, который:
  -- хранит список игроков;
  -- составляет пары на тур;
  -- запускает очередной тур;
  -- обновляет турнирную таблицу;
  -- показывает лидеров;
  -- определяет победителя по итогам турнира.

- Логика начисления очков:
  -- победа = 1 очко;
  -- ничья = 0.5 очка;
  -- поражение = 0 очков.

- Дополнительно:
  -- реализуйте швейцарскую систему упрощённо: игроки с близкими очками играют друг с другом;
  -- запретите повторные пары;
  -- реализуйте случайную генерацию результата матча с учётом рейтинга игроков;
  -- добавьте тай-брейки: по количеству побед, по рейтингу, по личной встрече.

Пример классов:

----------------------------------------------------------------------------------------------------
'''
import datetime, random
class Player:
    def __init__(self, name):
        self.name = name
        self.rating = random.randint(100, 2000)  # random ratings so simulate_result is meaningful
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0

class Match:
    def __init__(self, pl1: Player, pl2: Player):
        self.pl1 = pl1
        self.pl2 = pl2
        self.result = None
        self.date = datetime.datetime.now()
        self.duration = random.randint(10, 120)

class Tournament:
    def __init__(self):
        self.players = []
        self.matches = []
        self.round_num = 0
        self.past_pairs = set()

    def add_player(self, pl: Player):
        self.players.append(pl)

    def hierarchy(self):
        return sorted(self.players, key=lambda p: (p.points, p.wins, p.rating), reverse=True)

    def show_hierarchy(self):
        print(f"\n--- Round {self.round_num} standings ---")
        for i, p in enumerate(self.hierarchy(), 1):
            print(f"{i}. {p.name}: points={p.points}, wins={p.wins}, rating={p.rating}")

    def update_points(self, p1: Player, p2: Player, result):
        if result == "p1":
            p1.wins += 1
            p1.points += 1
            p2.losses += 1
        elif result == "p2":
            p2.wins += 1
            p2.points += 1
            p1.losses += 1
        elif result == "draw":
            p1.draws += 1
            p2.draws += 1
            p1.points += 0.5
            p2.points += 0.5

    def simulate_result(self, p1: Player, p2: Player):
        draw_weight = 0.5 * (p1.rating + p2.rating) / 10
        res = random.choices(
            ["p1", "p2", "draw"],
            weights=[p1.rating, p2.rating, draw_weight])[0]
        return res

    def round(self):
        self.round_num += 1
        sorted_players = self.hierarchy()
        paired = []
        unpaired = sorted_players[:]

        while len(unpaired) >= 2:
            p1 = unpaired[0]
            unpaired.remove(p1)
            opponent = None
            for p2 in unpaired:
                pair_key = tuple(sorted((p1.name, p2.name)))
                if pair_key not in self.past_pairs:
                    opponent = p2
                    break
            if opponent is None:
                print(f"{p1.name} gets a bye this round")
                continue
            unpaired.remove(opponent)
            pair_key = tuple(sorted((p1.name, opponent.name)))
            self.past_pairs.add(pair_key)
            res = self.simulate_result(p1, opponent)
            self.update_points(p1, opponent, res)
            paired.append((p1, opponent))
p1 = Player("Shushan")
p2 = Player("Maka")
p3 = Player("Louis")
p4 = Player("John Galliano")
t = Tournament()
for i in (p1,p2,p3,p4):
    t.add_player(i)
t.round()
t.show_hierarchy()
t.round()
t.show_hierarchy()
t.round()
t.show_hierarchy()
