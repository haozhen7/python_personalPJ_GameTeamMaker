# 게임 팀 생성 프로젝트
# 아/브/실/골/플/에/다/마/그마/챌 10개의 티어( 티어는 점수 구분 1~10점, 팀 결정 시 점수 같으면 성공 )
# 라인은 탑 / 정글 / 미드 / 원딜 / 서폿 >> 각각 1~5번으로 구분
# 10명의 인원
# 5개의 라인
# 입력받는 정보는 이름 / 티어 / 희망하는 라인2개 
# 입력받아 두 팀을 생성하는데, 점수 합이 같아야 함. 라인이 겹치면 안됨.
# 결과값은 랜덤으로 생성
# 원하는 결과값
# 위와 같이 10회 반복
# 위 입력받은 인원들을 겹치는 라인별로
##### 팀 생성 프로그램 ##### 
# 이름 :  
# 티어 :  
# 희망라인 1:
# 희망라인 2:


# Team 1 
# 탑 : 이름,티어
# 정글 : 
# 미드
# 원딜
# 서폿

# Team 2
# 탑 :
# 정글
# 미드
# 원딜
# 서폿

# 위 팀으로 진행하겠습니까? y / n 
# if y == break / n == continue
# 위와 같이 출력
# 결과를 받고 마음에 들지 않을 경우, 반복문 처음으로 continue. 

import random # 먼저 파이썬 내장되어있는 랜덤함수를 사용할꺼니까 불러옴 ( 팀 뽑기, 인원뽑기 등등 )

TIERS = { # 티어의 종류를 저장시켜 입력받을 수 있는 티어 종류 딕셔너리에 저장
    "아이언":1,
    "아":1,
    "브론즈":2,
    "브":2,
    "실버":3,
    "실":3,
    "골드":4,
    "골":4,
    "플레티넘":5,
    "플":5,
    "에메랄드":6,
    "에":6,
    "다이아몬드":7,
    "다":7,
    "마스터":8,
    "마":8,
    "그랜드마스터":9,
    "그마":9,
    "챌린저":10,
    "챌":10,
}

POSITIONS = {1:"탑",2:"정글",3:"미드",4:"원딜",5:"서폿"} # 포지션은 각 번호에 할당시켜 딕셔너리에 저장

TIER_NAMES={ # 왜 사용? >>> 계산할 때 숫자로 입력받아 계산한 결과를 다시 사용자가 읽기 쉽게 문자열로 바꿔서 출력하기 위함
    1:"아이언",
    2:"브론즈",
    3:"실버",
    4:"골드",
    5:"플레티넘",
    6:"에메랄드",
    7:"다이아몬드",
    8:"마스터",
    9:"그랜드마스터",
    10:"챌린저",
}

def get_player_inputs(): # >> 플레이어 정보 입력받는 함수
    players = [] # 플레이어 라는 빈 리스트 생성
    print("##### 팀 생성 프로그램 #####\n") 
    print("라인 입력 가이드 : 1:탑 / 2:정글 / 3:미드/ 4:원딜 / 5:서폿\n") # 라인 입력 방식 안내

    for i in range(1,11): # 10명의 플레이어를 입력받기에 10번 반복
        print(f"--- {i}번째 플레이어 정보 입력 ---") # 1~10번째 플레이어까지 반복
        name = input("이름 :").strip() # .strip? > 양쪽 끝의 공백 제거함수

        while True: # 무한반복문을 통해 제대로된 티어 입력 받을때까지 반복
            tier_str = input("티어입력 : ").strip() 
            if tier_str in TIERS: # 입력받은 티어가 TIERS 딕셔너리에 존재한다면
                tier_score = TIERS[tier_str] # 해당 티어 점수를 딕셔너리에서 찾아 저장
                break # 다음 플레이어로 이동
            print("제대로된 티어 입력해라.")

        while True:
            try: # 잘못된 값을 입력했을 때, 강제종료를 막기 위해 고의적으로 사용자가 오류 생성하여 입력 
                p1 = int(input("희망라인 1 (1~5):")) # 희망라인을 정수 1~5사이값으로 입력받는다
                p2 = int(input("희망라인 2 (1~5):"))
                if p1 in POSITIONS and p2 in POSITIONS and p1 != p2: # 입력받은 희망 라인 두 개가 모두 POSITIONS 딕셔너리에 존재하고, 두 라인이 겹치지 않는다면,
                    break # 반복종룍 후 다음플레이어 이동
                print("1~5사이의 서로 다른 숫자를 입력해라.") 
            except ValueError: # 위 경우가 아닐 경우, 오류 출력
                print("숫자만 입력.") 

        players.append( # 올바르게 입력된 플레이어 정보는 위 players 리스트에 추가함
            {
                "name":name,
                "tier_score":tier_score,
                "tier_name":TIER_NAMES[tier_score],
                "pref":[p1,p2],
            }
        )
        print()

    return players # 저장된 플레이어 리스트 출력

def assign_roles(team_players): ## 이 코드는 완전 이해안됨
    """5명 팀원에게 희망라인 중복 없이 배정"""

    def dfs(idx, used_positions, current_assignment): ## idx : 라인을 정하고 있는 플레이어 번호(0~4)
                                                      ## used_postions : 앞서 정해진 라인 목록 
                                                      ## current_assignment : 몇 번 플레이어가 어느 라인을 맡았는지 저장하는 라인배열표
        if idx == 5: # 모든 배정이 끝났을 경우, 
            return current_assignment # 저장된 라인 배열표 출력

        player = team_players[idx] # 현재 순서에 해당하는 플레이어
        for p in player["pref"]: # 해당 플레이어의 희망라인(pref) 반복문에 넣어 확인
            if p not in used_positions: # 해당 희망라인이 정해진 라인 목록에 없다면, 아무도 해당 라인에 배정되지 않았다면,
                used_positions.add(p) # 해당 라인목록에저장
                current_assignment[p] = player # 라인 배열표에 저장
                res = dfs(idx + 1, used_positions, current_assignment) # 다음 선수(idx + 1)로 넘어가 같은 방식으로 실행
                if res: # 다음 선수들 전부 잘 배정된 결과(res)가 나왔다면,
                    return res # 계속해서 위로 결과를 전달함
                used_positions.remove(p) # 다음 선수 배정을 위해 올라갔는데 진행이 불가능할 경우,
                del current_assignment[p] # 앞서 정해진 라인 목록에서 해당 라인 제거 후 for문으로 돌아가 다시 시도?
        return None  #  1,2지망 둘 다 시도해봤는데 뒷사람과의 라인 합이 안맞아 실패했다면, 라인 겹치지 않게 배정이 불가능 = None실패 출력
    return dfs(0, set(), {}) # 정해진 결과값 출력

def generate_balanced_teams(players): 
    """평균 티어 점수가 같고, 라인이 모두 채워지는 팀 조합 생성"""
    import itertools # 이 내장함수 역할? >>> 조합, 순열, 반복(Iteration) 작업을 효율적으로 처리해 주는 표준 라이브러리

    valid_team_pairings=[] # 성공적인 팀 조합을 저장할 빈 리스트 생성

    # 10명중 5명을 선택하는 모든 조합
    indices = list(range(10)) # 리스트 길이 10인 리스트를 생성, 인덱스는 선수 번호
    for team1_indices in itertools.combinations(indices, 5): # 10명 중 5명을 순서 없이 뽑는 모든 조합 (총 252가지 경우의 수)
        team2_indices =[i for i in indices if i not in team1_indices] 
        # 10명중 5명을 선택해 team1 , 나머지는 team2로 나누기위해 itertools.combinations 사용


        team1_players = [players[i] for i in team1_indices] # team1의 플레이어 목록 저장
        team2_players = [players[i] for i in team2_indices] # team2의 플레이어 목록 저장

        # 평균 등급 (티어합) 비교

        score1 = sum(p["tier_score"] for p in team1_players) # team1플레이어들의 티어 점수 합 
        score2 = sum(p["tier_score"] for p in team2_players)

        if score1 == score2: # 각 팀의 티어점수를 비교하여 같다면
            # 두 팀 모두 희망 라인으로 5개 라인이 채워지는지 확인
            role1 = assign_roles(team1_players)
            role2 = assign_roles(team2_players)

            if role1 and role2: # 팀의 티어 점수가 같고, 희망라인으로 5개라인이 채워진다면, 성공적 팀 조합 저장
                valid_team_pairings.append((role1,role2))

    return valid_team_pairings


def print_team(team_num, role_dict): # 팀출력 함수 : 팀 번호, 위 함수에서 완성된 각 플레이어 딕셔너리 데이터
    print(f"\n# Team {team_num}") 
    for pos_num in range(1,6): # 1번~5번라인 까지 반복
        pos_name=POSITIONS[pos_num] # 라인 번호에 해당하는 라인 이름 가져옴
        p=role_dict[pos_num] # 해당 라인의 플레이어 딕셔너리 정보 가져옴
        print(f"#{pos_name} : {p['name']}, {p['tier_name']}") # 왜 대괄호를 또 안에 쓴거
        # >>> p라는 변수에 플레이어 한 명의 정보가 담김 딕셔너리가 들어있어 key-value값 형태 저장
        #  이로 인해 딕셔너리 안에 name키값만 출력하기 위함


def main():
    players = get_player_inputs()

    print("\n조건에 맞는 팀 조합 계산중...")
    valid_pairings = generate_balanced_teams(players)

    if not valid_pairings:
        print("\n[오류] 입력한 값으로는 결과 출력이 불가능합니다.")
        return
    # 마음에 들 때 까지 무한반복 (n누르면 무작위 재생성)
    
    while True:
        # 조건에 맞ㄴㄴ 조합 중 무작위 1개 선택
        team1_roles, team2_roles = random.choice(valid_pairings)

        print("\n=========================================")
        print_team(1, team1_roles)
        print_team(2, team2_roles)
        print("\n=========================================")

        answer = input("\n위 팀으로 진행하겠습니까? y / n : ").strip().lower() # lower?

        if answer == "y":
            print("\n 팀 구성이 완료되었습니다 ")
            break
        elif answer == "n":
            print("\n 팀을 재구성합니다")
        else:
            print(" y또는 n으로 입력해주세요 ")


if __name__ == "__main__":
    main()       

# 깃 변경사항 테스트 위한 변경 