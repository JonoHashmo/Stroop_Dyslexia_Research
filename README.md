# Does Color Get in the Way? Reverse Stroop Interference in Dyslexic vs. Normative Readers
This repository is a complete experiment consisting of a stroop and reverse stroop task, with suggested initial analysis, examining the difference in interference in a reverse stroop task between adults with dyslexia and normative readers.

## Stroop vs Reverse Stroop
A stroop task consists of the name of a color being shown on the screen, printed in various different ink colors. Sometimes the word and color are one and the same, the congruent condition (i.e. RED printed in red ink) and other times the color will be different, the incongruent condition (i.e. RED printed in blue ink). The task in a normal stroop test is to identify the ink color the word is printed in regardless of the color name (i.e. if the word RED is printed in blue color, the correct answer would be BLUE). 
A reverse stroop task consists of the reverse. Meaning, the participant must identify the color name being presented regardless of the ink color it is written in (i.e. if the word RED is printed in blue color, the correct answer would be RED). 

## Experiment Justification
Previous studies have shown that normative readers exhibit little to no interference in reverse stroop tasks (MacLeod, 1991). This has been perceived as evidence supporting the theory that reading is largely automatic. Regardless of the ink color the word is printed in, the word is being proccessed with no interference.
Because people with Dyslexia read slower, we hypothesize that the different ink color of the word will create higher interference rates when compared to normative readers. The slower reading process, regardless of its automatic nature, may introduce  interference for dyslexic adults. Research has shown that adults with dyslexia demonstrate deficits in inhibitory control and executive function (Proulx & Elmasry, 2015; Smith-Spark et al., 2016). This may make it more difficult for them to disregard the competing sensory input, in our case the differing ink color, when simply reading the world demands such effortful proccessing.

## Project Overview
This experiment uses a stroop and reverse stroop task to determine whether dyslexic individuals exhibit greater interference effects compared to healthy controls on the reverse stroop task. It uses a mixed design, with group (dyslexic vs. control) as a between-subjects factor and task type (Stroop vs. reverse Stroop) as a within-subjects factor. The primary interest in our study is in comparing interference rates between groups, and especially in the group × task type interaction. For instance, whether dyslexic readers show disproportionately more interference on one task compared to the other, which could help shed light on differences in interference and reading automaticity. The within-subjects comparison of interference across stroop and reverse stroop tasks within each participant is also available for those interested in exploring the interference asymmetry further on its own.

## Required Files
This experiment expects specific folder names, file names, and column names in order to run properly. All of these are in this repository. The folder, file, and column names below must remain unchanged, though the content is customizable (discussed below).
- `conditions_csv_files/`– folder containing the four conditions CSV files:
  - `stroop_conditions.csv`
  - `reverse_stroop_conditions.csv`
  - `practice_stroop.csv`
  - `practice_reverse_stroop.csv`
  - In these files, column names `word`, `color`, `condition`, and `correct_key` must stay the same.
- `instruction_txt_files/` - folder containing all welcome, instructions, and end-of-experiment text files. The names of the following files must stay the same:
  - `intruct_stroop_first.txt`
  - `intruct_revstroop_first.txt`
  - `instruct_revstroop_second.txt`
  - `instruct_stroop_second.txt`
  - `pre_exp_text.txt`
  - `pre_exp_second_text.txt`
  - `end_text.txt`
- `participants.csv` – file containing all participant information. The following column names must stay the same: `participant_nr`, and `group` (see Participants section).
- `results/` – folder that will contain the participant’s results CSVs. This folder must exist, even if empty, before the experiment begins for the code to work properly.

## Experimental Design
### Variables
**Independent Variables:**
- Group (dyslexic vs. control) 
- Task type (stroop vs. reverse stroop) 
- Condition (congruent vs. incongruent)
**Dependent Variables:**
- Reaction time (for correct responses)
- Accuracy (percent correct)

### Experimental Blocks
- Each participant completes 2 blocks: one stroop and one reverse stroop. Each block is preceded with a practice round and instructions.
- Stroop and reverse stroop order is counterbalanced by participant number: odd-numbered participants complete stroop first and even-numbered participants complete reverse stroop first. 
- Blocks contain 128 trials each, with a mix of congruent (same color word and ink) and incongruent (different color word and ink) conditions.
- Because of the complexity of the task, practice trials provide feedback to participants who get the answer wrong (i.e. “Incorrect – try again!”) and require participants to get all correct trials before moving on to the experiment phase. 
- Experimental blocks, naturally, do not provide feedback and record accuracy and reaction time.

### Participants
This experiment expects participant information to be stored in a CSV file that must be called participants.csv. This file must contain the following columns:
- `participant_nr`: any integer
- `group`: groups can be separated in any way that makes sense to the researcher. In the example file we decided to have “control” vs “dyslexic”. The code will migrate these values into the results file generated at the end. 

This information can be gathered ahead of time through a Qualtrics questionnaire, standardized assessments, or other screening methods. The included participants.csv file contains 5 example rows for reference. 

### Parameters
- Colors: Red, Blue, Green, Yellow
- Key mappings: D=Red, F=Blue, J=Green, K=Yellow
- Trials per block: 128
- Fixation duration: random intervals between 0.5 and 1 seconds

### Customizations
This experiment is designed to be easily modifiable to address any changes in the hypothesis being tested. 

**Trial Count and Condition**
The total number of trials, as well as the ratio of congruent and incongruent conditions are controlled by the CSV files in the `conditions_csv_files` (`stroop_conditions.csv` and `reverse_stroop_conditions.csv`). To edit these conditions, simply edit the csv files, but do not remove them from the folder or change their names. The same can be done with the practice CSV files. 
Similarly, all welcome, instruction, and end texts can be edited by navigating to the `instruction_txt_files` folder and editing the respective TXT file. Note that all file names should remain the same and not be moved out of the folder. 

**Fixation Duration**
In this experiment, the fixation cross currently displays for an interval between 0.5 seconds and 1 second. This is set using the piece of code below in the Stroop() function.
```python
random.uniform(0.5, 1)
```
This range can be adjusted in the Experiment.py file. 

### Running the Experiment
1. Download the experiment file into the working directory on your console.
2. Run the experiment using Terminal:
```bash
python3 Experiment.py
```
3. Enter the participant number in the dialogue box. (This participant number must match the participants.csv file. This is caught in a try/except loop).
4. Have participants follow the on screen instructions.
5. Experiment results will be exported to the results folder.

## Experiment Controls
- Participants will be prompted to use the ‘space’ bar in order to move between instruction screens and in order to start the experiment.
- Keys for colors will be explained in the beginning of the experiment, and be included below the target word as a reminder.
- The ‘ESC’ key can be used by facilitators to terminate the experiment at anytime. 

### Results and Analysis 
Two files will be created at the conclusion of the experiment. Both will be located in the `results` folder in the working directory.
- `participant_X_results.csv` – This CSV file contains all trials for each participant in a long format. It contains the participant number, group, stroop type, trial number, word printed, ink color, type of condition, the correct key that should be pressed, the participant’s pressed key, reaction time, and whether they got this trial correctly or not.
- `participant_X_summary_results.csv` – This CSV file contains some summary statistics for each participant with one row per stroop type and condition combinations. It contains the participant number, the stroop type and condition, the total number of trials in each category, the number of correct trials, the average reaction time, and the percent of trials that were answered correctly. 

Below are screenshots of the two results CSV files. 

`participant_102_results.csv` exmaple:
<img width="820" height="364" alt="102 example results" src="https://github.com/user-attachments/assets/401138d7-1258-488b-a221-ae34893dc64b" />

`participant_102_summary_results.csv` example:
<img width="659" height="103" alt="102 example resutls summary" src="https://github.com/user-attachments/assets/2a8262b7-047c-447c-b85c-e97e8107cb0f" />

### Enjoy the experiment!!

## References
- MacLeod, C. M. (1991). Half a century of research on the Stroop effect: An integrative review. Psychological Bulletin, 109(2), 163–203. https://doi.org/10.1037/0033-2909.109.2.163
- Proulx, M. J., & Elmasry, H.-M. (2015). Stroop interference in adults with dyslexia. Neurocase, 21(4), 413–417. https://doi.org/10.1080/13554794.2014.914544
- Smith-Spark, J. H., Henry, L. A., Messer, D. J., Edvardsdottir, E., & Zięcik, A. P. (2016). Executive functions in adults with developmental dyslexia. Research in Developmental Disabilities, 53–54, 323–341. https://doi.org/10.1016/j.ridd.2016.03.001
