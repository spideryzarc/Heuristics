# %%
import random as rd

num_queens = 50 # número de rainhas
current_solution = {} # guardando a solução corrente na coluna i, i = 1,2...,num_queens
list_choices = {} # lista de possíveis escolhas na coluna i, i=1,2..num_queens

# %%
def get_key_dict(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

# retorna um conjunto de soluções possíveis para uma coluna, dependendo das aosluções anteriores
def populate_choices(i):
    list_choices = [i for i in range(num_queens)]
    print(f'vetor de soluções: {current_solution}')
    #print(list_choices)
    for j in range(i):
        #print(f'Solução {j}')
        step_diag = i-j
        if current_solution[j] in  list_choices:
            list_choices.remove(current_solution[j])
        #print(f'Solução anterior deletada: {current_solution[j]}' )
        #print(f'Diagonais deletadas: {(current_solution[j]-step_diag)} e {(current_solution[j] + step_diag)}')
        
        check_lower = current_solution[j]- step_diag >=0
        check_upper = current_solution[j] < num_queens

        if check_lower:
            if (current_solution[j]- step_diag) in list_choices:
                list_choices.remove(current_solution[j]- step_diag)
          
        if check_upper:
            if (current_solution[j] + step_diag) in list_choices:
                list_choices.remove(current_solution[j]+ step_diag)
        #print(list_choices)
    return list_choices


# %%
# Essa função retorna uma solução aleatória para a primeira coluna
def first_solution(num_queens):
    
    print(f"Coluna 0: ")

    list_choices[0] = [j for j in range(num_queens)]
    current_solution[0] = rd.choice(list_choices[0])
    
    print(f'Póssíveis escolhas na coluna 0: {list_choices[0]}')
    print(f'Valor escolhido aleatóriamente: {current_solution[0]}')
    print('*'*10)

    list_choices[1] = populate_choices(1)

    print(f'Póssíveis escolhas na coluna 1: {list_choices[1]}')
    calculate_solution(1, list_choices)

# Essa função recalcula a solução a partir de uma coluna i.
def calculate_solution(start_column, list_choices):

    if len(list_choices[start_column])==0:
        list_choices[start_column-1].remove(current_solution[start_column-1])
        print('*'*10)
        print(f'Recalculando a partir da coluna {start_column - 1}')
        print('*'*10)
        calculate_solution(start_column-1, list_choices)
    else:
        current_solution[start_column] = rd.choice(list_choices[start_column])
        print(f'Valor escolhido aleatóriamente: {current_solution[start_column]}')
        print('*'*10)
        
        list_choices[start_column + 1] = populate_choices(start_column + 1)
        
        if start_column +1 < num_queens:
            print(f'Póssíveis escolhas na coluna {start_column+1}: {list_choices[start_column+1]}')
            calculate_solution(start_column + 1, list_choices)
        else:
            return current_solution

if __name__ == '__main__':
    solution = first_solution(num_queens)


# %%
