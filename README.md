# A tool to handle dataset imbalance 
## Method
Oversampling minority and undersampling majority [link](https://towardsdatascience.com/solving-the-class-imbalance-problem-58cb926b5a0f#:~:text=Imbalanced%20classification%20is%20a%20common,bias%20in%20the%20trained%20model.)  

## Dataset
Design for the [HA-ViD](https://github.com/iai-hrc/ha-vid) action recognition dataset. The tool may be applicable to mmaction2 datasets.

## Usage
1. copy the repo
2. open `file_mover.py`, and replace the folder path. The class proportions will show in a pie chart. Removed files will be saved in `temp_videos`
3. open `train_list_merge_tool.py`, and replace the `file_a_path` to be the annotation file path, the new annotation file will be `output.txt` under same folder

## Note
The video folders will be modified (video duplicate or remove), backup folder in advance may be needed.
