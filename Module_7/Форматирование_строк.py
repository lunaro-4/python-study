def one_team_string(name: str, team1_num: int) -> str:
    final_string: str = "В команде %s участников %i"
    return (final_string % (name, team1_num))

def multiple_teams_string(*teams) -> str:
    final_string: str = "Итого сегодня в коммандах участников: %i"
    total_teams: int = len(teams)
    if total_teams == 0:
        return ""
    elif total_teams == 1:
        final_string += "!"
        return (final_string % teams[0])
    for _ in range(1, total_teams - 1):
        final_string += ", %i"

    final_string += " и %i!"

    return (final_string % teams)


def format_one_team(name: str, score_2: int) -> str:
    final_string: str = "Комманда {name} решила задач: {score}".format(name=name, score=score_2)
    return final_string

def format_multiple_teams(**team_to_time) -> str:
    final_string: str = "Результаты соревнований на время:"
    for team, time in team_to_time.items():
        team_score_str: str = "\n{name} решили задачи за {time}".format(name=team, time=time)
        final_string += team_score_str
    return final_string



def f_multiple_teams_string(*results) -> str:
    final_string: str = "Команды решили "
    total_teams: int = len(results)
    if total_teams == 0:
        return ""
    elif total_teams == 1:
        final_string += (f"{results[0]}")
        return (final_string + " задач")
    final_string += (f"{results[0]}")
    for i in range(1, total_teams -1 ):
        final_string += (f", {results[i]}")
    final_string += f" и {results[total_teams-1]}"
    return (final_string + " задач")


def f_challange_result(**teams_score) -> str:
    leader_team: str = ''
    leader_score: float = 0
    is_tie = False
    tie_leaders: list[str] = []
    for team, score in teams_score.items():
        if score > leader_score:
            leader_score = score
            leader_team = team
            tie_leaders.clear()
            tie_leaders.append(team)
            is_tie = False
        elif score == leader_score:
            is_tie = True
            tie_leaders.append(team)

    if is_tie:
        return f"Ничья между {''.join(tie_leaders[:-1])} и {tie_leaders[-1]}"

    return (f"Результат битвы: победа команды {leader_team}!")

def f_tasks_total(tasks: int, avg_time: float) -> str:
    return f"Сегодня было решено {tasks} задач, в среднем по {avg_time}"
    


