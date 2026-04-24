from psychopy import event, data
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim
from psychopy.core import Clock, quit, wait
from psychopy.hardware.keyboard import Keyboard
import random
import pandas as pd
import os

### Define Stroop Task ###
def Stroop(rev=True, practice = False): # no practice default. rev=True (default): reverse stroop, rev=False: regular stroop
    if practice:
        if rev:
            trial_df = pd.read_csv(os.path.join('conditions_csv_files','practice_reverse_stroop.csv'))
        else:
            trial_df = pd.read_csv(os.path.join('conditions_csv_files','practice_stroop.csv'))
    else:
        if rev:
            trial_df = pd.read_csv(os.path.join('conditions_csv_files','reverse_stroop_conditions.csv')).sample(frac=1).reset_index(drop=True)
            s_type = 'reverse'
        else:
            trial_df = pd.read_csv(os.path.join('conditions_csv_files','stroop_conditions.csv')).sample(frac=1).reset_index(drop=True)
            s_type = 'stroop'

    kb = Keyboard() #get Keyboard

    clock = Clock() # start clock

    key_rem = TextStim(win, 'D = Red, F = Blue, J = Green, K = Yellow', pos = (0,-0.09), height = 0.07)
    #create fixation
    fix_target = TextStim(win, '+')

    for i, row in trial_df.iterrows():

        #call fixation
        fix_target.draw()
        win.flip()
        wait(random.uniform(0.5,1))

        #clear clock and keboard
        clock.reset()
        kb.clearEvents()

        #Stroop
        word = TextStim(win, row['word'].upper(), color = row['color'], height = 0.1, bold = True)
        word.draw()
        key_rem.draw()
        win.flip()
        kb.clock.reset()

        #get participant response
        while True:
            keys = kb.getKeys(['d', 'f', 'j', 'k', 'escape'])
            correct = None
            if keys:
                resp = keys[0].name
                rt = keys[0].rt
                if resp == 'escape': #emergency exit
                    win.close()
                    quit()
                if row['correct_key'].lower() in keys:
                    correct = 'correct'
                    break
                else:
                    correct = 'incorrect'
                    if practice:
                        feedback = TextStim(win, 'Incorrect — try again!', color='red')
                        feedback.draw()
                        win.flip()
                        wait(1)
                        kb.clearEvents()
                        word.draw()
                        key_rem.draw()
                        win.flip()
                        kb.clock.reset()
                    else:
                        break
        if not practice:
            result_row = [participant_nr, group, s_type, len(results)+1, row['word'], row['color'], row['condition'], row['correct_key'], resp, rt, correct]
            results.loc[len(results)] = result_row

### Get Participant Information ###
participants_df = pd.read_csv('participants.csv')
## DIALOG BOX ROUTINE
while True:
    exp_info = {'participant_nr':'',}
    dlg = DlgFromDict(exp_info)

    if not dlg.OK:
        print("User pressed 'Cancel'!")
        quit()
    try:
        participant_row = participants_df[participants_df['participant_nr'] == int(exp_info['participant_nr'])] #take the integer form of the participant number in the .csv file of participants
    except:
        print("Please enter a number")
        continue
    ## make sure participant ID is valid
    if len(participant_row) == 0 :
        print("Participant ID not found in participants.csv. Enter a valid Participant ID.")
        continue
    else:
        participant_nr = int(exp_info['participant_nr'])
        group = participant_row['group'].values[0] #get whether the participant is in the dyslexic or control groups
        break

print(f"Started experiment for participant {exp_info['participant_nr']}. They are in the {group} group.")

### Create results data frame ###
results = pd.DataFrame(columns=['participant_nr', 'group', 'stroop_type', 'trial_nr', 'word', 'color', 'condition', 'correct_key', 'pressed_key', 'rt', 'correct'])

### Assign Order of Stroop Tasks ###
if int(exp_info['participant_nr']) % 2 == 0: #if odd participant number, Stroop first.
    order = ['reverse_stroop', 'stroop']
else:
    order = ['stroop', 'reverse_stroop']


win = Window(size=(800, 400), fullscr=True)

### WELCOME ROUTINE ###
welcome_txt_stim = TextStim(win, text="Welcome to this experiment!")
welcome_txt_stim.draw()
win.flip()
wait(2)

### INSTRUCTION ROUTINE ###

if order[0] == 'stroop':
    with open(os.path.join('instruction_txt_files','intruct_stroop_first.txt'), 'r') as x:
        task_instruct_txt = x.read()
else:
    with open(os.path.join('instruction_txt_files','intruct_revstroop_first.txt'), 'r') as x:
        task_instruct_txt = x.read()

# Show instructions and wait until response (return)
task_instruct_txt_show = TextStim(win, task_instruct_txt, alignText='left', height=0.07, wrapWidth=1.8, pos=(0, 0))
task_instruct_txt_show.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'space' in keys:
        break
    elif 'escape' in keys:
        quit() #emergency exit

### Practice ###
if order[0] == "stroop":
    Stroop(rev=False, practice = True)
else:
    Stroop(rev=True, practice=True)

### Pre-Experiment, post practice text ###
with open(os.path.join('instruction_txt_files','pre_exp_text.txt'), 'r') as x:
    pre_exper_instruct = x.read()

pre_exper_instruct_show = TextStim(win, pre_exper_instruct, alignText='left', height=0.07, wrapWidth=1.8, pos=(0, 0))
pre_exper_instruct_show.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'space' in keys:
        break
    elif 'escape' in keys:
        quit() #emergency exit

### Start First Experiment ###
if order[0] == "stroop":
    Stroop(rev = False, practice = False)
else:
    Stroop(rev = True, practice = False)

#print(results)

### Second Experiment Instructions ###
if order[0] == 'stroop':
    with open(os.path.join('instruction_txt_files','instruct_revstroop_second.txt'), 'r') as x:
        task_instruct_txt = x.read()
else:
    with open(os.path.join('instruction_txt_files','instruct_stroop_second.txt'), 'r') as x:
        task_instruct_txt = x.read()

# Show instructions and wait until response (return)
task_instruct_txt_show = TextStim(win, task_instruct_txt, alignText='left', height=0.07, wrapWidth=1.8, pos=(0, 0))
task_instruct_txt_show.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'space' in keys:
        break
    elif 'escape' in keys:
        quit() #emergency exit

### Start Second Experiment practice ###
if order[0] == "stroop":
    Stroop(rev=True, practice = True)
else:
    Stroop(rev=False, practice=True)

### Pre-Experiment, post practice text ###
with open(os.path.join('instruction_txt_files','pre_exp_second_text.txt'), 'r') as x:
    pre_exper_instruct = x.read()

pre_exper_instruct_show = TextStim(win, pre_exper_instruct, alignText='left', height=0.07, wrapWidth=1.8, pos=(0, 0))
pre_exper_instruct_show.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'space' in keys:
        break
    elif 'escape' in keys:
        quit() #emergency exit

### Start Second Experiment ###
if order[0] == "stroop":
    Stroop(rev = True, practice = False)
else:
    Stroop(rev = False, practice = False)

#print(results)

### Export results into a CSV file ###
results.to_csv(os.path.join('results', f"participant_{participant_nr}_results.csv"), index=False)

### Basic analysis ###
correct_results = results[results['correct'] == 'correct'] #find correct results

correct_results_summary = results.groupby(["stroop_type", "condition"]).agg(
    total_trials = ("correct", "count"), #get the total number of trials
    total_correct = ("correct", lambda x: (x == "correct").sum()), #get the total number of correct trials
).reset_index()

mean_rt = correct_results.groupby(["stroop_type", "condition"])["rt"].mean().reset_index()

results_summary = correct_results_summary.merge(mean_rt, on=["stroop_type", "condition"])

## add participant number and percent correct for each condition and stroop type.
results_summary.insert(0, "participant_nr", participant_nr)
results_summary["percent correct"] = correct_results_summary["total_correct"]/correct_results_summary["total_trials"]

## export.
results_summary.to_csv(os.path.join('results', f"participant_{participant_nr}_summary_results.csv"), index=False)

### End Text ###
with open(os.path.join('instruction_txt_files','end_text.txt'), 'r') as x:
    end_text = x.read()

pre_exper_instruct_show = TextStim(win, end_text, alignText='center', height=0.07, wrapWidth=1.8, pos=(0, 0))
pre_exper_instruct_show.draw()
win.flip()

wait(10)

quit()
