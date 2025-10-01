close all;
clear all;

step=100


p(1)=0;


    
for i = 1:step-1
    
 
    
    if rand(1)>0.5
            p(i+1)=p(i)+1;
    else 
            p(i+1)=p(i)-1;
         
    end
        
    
    
   
end




plot(p,'g','LineWidth',1)


xlabel('Steps taken')

ylabel('random Walkers position (p)')
grid on
title('Random walk in 1 D ')
