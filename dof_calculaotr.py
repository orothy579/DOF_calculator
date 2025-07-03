print("자유도 계산기")
n = int(input("링크의 개수를 입력하세요 : "))
j = int(input("조인트의 개수를 입력하세요 : "))

f = []  # joint_dofs

for i in range(j):
    tmp = int(input(f"{i + 1}번 관절의 자유도를 입력하세요 : "))
    f.append(tmp)


def calculate_dof(num_links, num_joints, joint_dofs):
    m = 6  # 3D 공간에서 링크가 가질 수 있는 최대 자유도는 6
    # Kutzbach Formula 적용
    F = m * (num_links - num_joints - 1) + sum(joint_dofs)
    return F


F = calculate_dof(n, j, f)

print(f"계산된 자유도 : {F}")
