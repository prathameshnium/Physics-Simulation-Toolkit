close all;
clear all;

step=10


x(1)=0
y(1)=0



    
    
for i = 1:step
    
 
    
    if rand(1)>0.5
            x(i+1)=x(i)+1;
    else 
            x(i+1)=x(i)-1;
        
        
    end
        
    
    
   
end


for j = 1:step
    
 
    
    if rand(1)>0.5
            y(j+1)=y(j)+1;
    else
            y(j+1)=y(j)-1;
        
        
    end
        
    
    
   
end


plot(x,y)
grid on
