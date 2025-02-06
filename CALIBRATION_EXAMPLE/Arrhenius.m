clear all
close all
clc

%VC25
% E=76701.0;
% R=8.314;
% S=679.0;
% H=203791.0;
% 
% for t=1:50
%     Res1(t)=exp(E*(t-25)/298/R/(t+273))*(1+exp((298*S-H)/298/R))/(1+exp((S*(t+273)-H)/R/(t+273)));
% end
% 
% hold on
% plot(Res1)
% 
% E2=56701.0;
% R=8.314;
% S2=479.0;
% H2=139791.0;
% 
% for t=1:50
%     Res2(t)=exp(E2*(t-25)/298/R/(t+273))*(1+exp((298*S2-H2)/298/R))/(1+exp((S2*(t+273)-H2)/R/(t+273)));
% end
% 
% hold on
% plot(Res2)

%J
% E=51049.0;
% R=8.314;
% S=680.0;
% H=205069.0;
% 
% for t=1:50
%     Res1(t)=exp(E*(t-25)/298/R/(t+273))*(1+exp((298*S-H)/298/R))/(1+exp((S*(t+273)-H)/R/(t+273)));
% end
% 
% hold on
% plot(Res1)
% 
% E2=31049.0;
% R=8.314;
% S2=420.0;
% H2=125069.0;
% 
% for t=1:50
%     Res2(t)=exp(E2*(t-25)/298/R/(t+273))*(1+exp((298*S2-H2)/298/R))/(1+exp((S2*(t+273)-H2)/R/(t+273)));
% end
% 
% hold on
% plot(Res2)

%TPU
E = 47100.0;
R=8.314;

for t=1:50
    Res1(t)=exp(E*(t-25)/298/R/(t+273));
end

hold on
plot(Res1)
