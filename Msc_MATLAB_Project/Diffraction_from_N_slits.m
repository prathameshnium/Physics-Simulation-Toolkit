close all;
clear all;


%n=5;

e=3

d=20


% A is alpha ,B beta , l lambda , thita t 
% n is the number of slits ,e is width of slit,d is width of opaque space/area,


l=5

%N=n;

Amp=10;

t1=linspace(1,2*pi,10000);



for N=[2 4 6 8]
    
    for ind=1:10000;
    
        t=t1(ind);

        A1(ind)=(pi*e*sin(t))/(l);
   
   
        B1(ind)=(pi)*(e+d)*sin(t)/(l);
    
  
        A=A1(ind);
        B=B1(ind);
        R(ind)=(Amp*sin(A)*sin(N*B))/(A*sin(B));
        I(ind)=R(ind)*R(ind);
        
    end
    

subplot (2,2,N/2)

plot(sin(t1),I)




xlabel('Sin(\theta)')

ylabel('Intensity I')
grid on


%{



x = [0 0.2 0.45 0.7 0.9];
y = [4.3 4 3.4 2.4 1.6];
y=1:5
labels = {'n=0','n=1','n=2','n=3' ,'n=4'};
text(x,-y+N), labels)

%}
   
end


subplot (2,2,1)
title('2 Slit diffraction')


subplot (2,2,2)
title('4 Slit diffraction')


subplot (2,2,3)
title('6 Slit diffraction')


subplot (2,2,4)
title('8 Slit diffraction')
