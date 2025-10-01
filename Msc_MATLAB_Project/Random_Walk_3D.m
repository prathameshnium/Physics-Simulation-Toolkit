close all;
clear all;


step=1
h=step/2

x(1)=0
y(1)=0
z(1)=0



    
    
    
for i = 1:step
  
    
    if rand(1)>0.5
            k1=-1;
    else 
            k1=+1;
        
        
    end
        
    
    x(i+1)=x(i)+k1;
   
end


for j = 1:step
    
 
    
    if rand(1)>0.5
            k2=-1;
    else
            k2=+1;
        
        
    end
        
    
    y(j+1)=y(j)+k2;
   
end


for k = 1:step
    
 
    
    if rand(1)>0.5
            k3=-1;
    else
            k3=+1;
        
        
    end
        
    
    z(k+1)=z(k)+k3;
   
end


%y=-h:h
plot3(x,y,z)
