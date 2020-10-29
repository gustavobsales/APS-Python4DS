import pandas as pd
from siuba import *
from plotnine import *

# Downloading databases

tuition_cost = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-10/tuition_cost.csv')
tuition_income = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-10/tuition_income.csv')
salary_potential = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-10/salary_potential.csv')
historical_tuition = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-10/historical_tuition.csv')
diversity_school = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-10/diversity_school.csv')

# Setting standard ggplot theme

theme_set(theme_bw())

# Exploratory analysis

order_states = (tuition_cost >>
                group_by(_.state) >>
                summarize(avg_room_board = _.room_and_board.mean()) >>
                arrange(_.avg_room_board)).state.tolist()

(tuition_cost >>
    mutate(state = pd.Categorical(tuition_cost["state"], categories=order_states)) >>
    group_by(_.state) >>
    summarize(avg_room_board = _.room_and_board.mean()) >>
    ggplot(aes("state", "avg_room_board")) +
    geom_col(aes(fill = "state"), show_legend = False) +
    coord_flip() +
    labs(x = "Average cost ($)",
         y = "",
         title = "Average cost of Room and Dorm"))