getwd()
setwd("~/Seminario Rodrigo/Clases Rodrigo/Códigos de clases")
my_data<-read.csv("bd_train2.csv")
str(my_data)
my_data$y<-as.factor(my_data$Comp_final)

modelb<-glm(y~.- Comp_final,data = my_data,family = binomial)
summary(modelb)
step(modelb)
library(dplyr)
library(MASS)
step.modelb <- modelb %>% stepAIC(trace = FALSE)
step.modelb


modelc<-glm(y~.- Comp_final- woe_comp_interno1 -woe_comp_externo2,data = my_data,family = binomial)
summary(modelc)
step(modelc)
step.modelc <- modelc %>% stepAIC(trace = FALSE)
step.modelc

modeld<-glm(y~.- Comp_final- woe_comp_interno1 -woe_comp_externo1,data = my_data,family = binomial)
summary(modeld)
step(modeld)
step.modeld <- modeld %>% stepAIC(trace = FALSE)
step.modeld