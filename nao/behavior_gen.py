from pyshop.pyshop import PyShop
from pyshop.pyshop import State
import send_actionscript
import json
import argparse
import sys




def scenario1(state1,ps):
    #Scenario-1 offer-help-question
    state1.add(["confusion", "early"])
    state1.add(["level", "l2"])

    return plan(state1, [["inquire", "misty"]], ps)

def scenario2(state1,ps): #test persist doing-great
    state1.add(["time", "long"])
    state1.add(["level","l2"])
    state1.add(["game", "no-error"])

    return plan(state1, [["persist", "misty"]], ps)

def scenario3(state1, ps): #test correct not-touching
    state1.add(["game", "not-touching"])
    return plan(state1, [["correct", "misty"]], ps)

def scenario4(state1, ps): #test instruct level 3 missing
    state1.add(["needsToBe", "blue small triangle", "missing", "found"])
    state1.add(["level","l3"])
    return plan(state1, [["instruct", "misty"]],ps)


def scenario5(state1, ps): #test instruct level 4
    state1.add(["needsToBe","small blue triangle", "spin", "right"])
    state1.add(["level", "l4"])
    return plan(state1, [["instruct", "Misty"]], ps)

def scenario6(state1, ps): #test intro 
    state1.add(["intro", "2"])
    return plan(state1, [["greeting", "Misty"]], ps)

def scenario7(state1, ps): #test confirm
    #state1.add(["interaction", "short"])
    state1.add(["level", "l1"])
    return plan(state1, [["confirm", "misty"]], ps)

def scenario8(state1, ps): #test instruct level 3
    state1.add(["needsToBe","small blue triangle", "spin", "left"])
    state1.add(["level", "l3"])
    return plan(state1, [["instruct", "Misty"]], ps)

def scenario9(state1, ps): #test instruct level 3
    state1.add(["level", "l2"])
    return plan(state1, [["missingPiece", "Misty"]], ps)


def scenario10(state1, ps): #test instruct swap
    state1.add(["needsToBe", "red medium triangle", "swap", "large orange triangle"])
    state1.add(["level", "l4"])
    return plan(state1, [["instruct", "Misty"]], ps)

def scenario11(state1, ps): #test instruct move
    state1.add(["needsToBe", "red medium triangle", "move", "lowerRight"])
    state1.add(["level", "l4"])
    return plan(state1, [["instruct", "Misty"]], ps)


def scenario12(state1, ps): #test release turn 
    state1.add(["gaze", "away"])
    state1.add(["affect", "negative"])
    return plan(state1, [["take-turn", "misty"]], ps)


def scenario13(state1, ps): #test relase turn
    state1.add(["gaze", "away"])
    state1.add(["affect", "negative"])
    return plan(state1, [["release-turn", "misty"]], ps)

def scenario14(state1, ps):
    state1.add(["level","l1"])

def plan(state, task, ps):
    return ps.pyshop(state, task, 3)


def init_planner(filePath):
    ps = PyShop('init')

    ps.declare_methods(filePath)   
    ps.declare_operators(filePath)  
    
    ps.print_operators()
    ps.print_methods()
    
    return ps
    

def plan_converter(plan):

    if plan == False:
        return False # if there is no plan


    dictionary_list = []
    for line in plan:
    
        dict = {}
        action = line[0]
        key = action[0]
        val = action[1:]
        dict['name'] = key
        dict['args'] = val

        dictionary_list.append(dict)

        json_obj = json.dumps(dictionary_list)
    return dictionary_list

def run_test(function, on_robot):

    state1 = State("1")
    data = plan_converter(function(state1, ps))
      
    if on_robot:
        nao.executeActionScript(data)
        print("Action executed!")


if __name__ == '__main__':

    #runTest()
    parser = argparse.ArgumentParser()
    parser.add_argument('test', default='test1', nargs='?')
    parser.add_argument('--file', default='misty.hddl')
    parser.add_argument('--address', default='192.168.1.3')
    parser.add_argument('--interactive', action='store_true')
    parser.add_argument('--robot', action='store_true')
    args = parser.parse_args()
    
    ps = init_planner(args.file)
    
    if args.robot:
        nao = send_actionscript.Nao(args.address)
        nao.startSkill()

    if args.interactive:
        state1 = State("interactive")
        state1.add(["level", "l4"])
        state1.add(["taskState","unstarted"])
        state1.add(["gaze","task"])
        state1.add(["rapport","medium"])
        state1.add(["affect","neutral"])
        state1.add(["needsToBe", "small blue triangle", "slide", "right"])
        state1.add(["intro","8"])
        state1.add(["verbal", "hello"])
    


        last_plan = ''
        user_input = ''
        while user_input != 'quit':
            user_input = input('Enter command (add, remove, list, plan, quit):')

            if len(user_input) == 0:
                user_input = last_plan

            if (user_input[0] == "a"):
                #add_fact = input ('add a fact in the format of [level, l2]: ')
                add_fact= user_input[2:]
                add_fact = add_fact.strip('][').split(', ')
                for fact in state1.facts:
                    if (fact[0] == add_fact[0]):
                        state1.remove(fact)
                state1.add(add_fact)

            if (user_input[0] == "r"):
                #rm_fact = input('Enter the number of the fact to remove:')
                rm_fact = user_input[2:]
                for fact in state1.facts:
                    if (fact[0] == rm_fact[0]):
                        state1.remove(fact)

            if (user_input[0] == "l"):
                print(state1.facts)

            if (user_input[0] == "p"):
                #task = input ('Enter task in the format [instruct, misty]: ')
                last_plan = user_input
                task = user_input[2:]
                task = task.strip('][').split(', ')

                iplan = plan(state1, [task], ps)
                data = plan_converter(iplan)
                
                if data == False:
                    print ("There is no plan for this task")
                    continue

                if args.robot:
                    nao.executeActionScript(data)
    


            if user_input == 'quit':
                break
        

    else:
        test_id = args.test[4]
        func = vars()["scenario"+str(test_id)]
        run_test(func, args.robot)




