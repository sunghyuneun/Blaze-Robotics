#include <iostream>

int main()
{
    std::cout << "Hello World!";
}



Why Capacitor is connected with DC Motor


You may notice that a small value of the ceramic capacitors are connected in parallel with small DC motors but why? In AC motors, capacitors are used to improve power factor but why capacitor is used in DC motors? Today we are going to discuss about it.

There are some important reasons why capacitor is used in DC motor which are explained below.


(1)The first and main reason is to reduce interference and noise. When the motor is in running condition, there is very frequent connection and disconnection happens between the brush and commutator. So the motor armature winding also connects and disconnects to the power supply frequency. This connection and disconnection are happening too fast. For this reason, the changes in motor current also happen too fast which creates magnetic interference and create disruption in nearby radio devices such as FM and AM receivers.

So to reduce this interference, a capacitor is connected across the motor terminals. The capacitor reduces the spikes in the motor current and reduces the magnetic interference.



(2)When DC motors are driven with digital signals then inductor or capacitor is always used with the DC motor. For example when a DC motor is driven with PWM(Pulse Width Modulation)signals, then the power supply to the motor frequently changes.  So the motor current also changes which will produce noise and interference. In this case also, the capacitor is used to reduce the noise and interference.


(3)The capacitor smoothens the rotation of the motor during the frequent changes in motor load. When frequent changes occur in the motor load then the motor draws a frequently changing current from the power supply. Here the capacitor helps to keep constant the motor current and smooth the motor speed.


(4)The capacitor absorbs the back emf of the motor and keeps healthy the power circuit. When the power supply is suddenly off, the motor does not stop immediately, in this case, the motor acts as a generator and produces the reverse voltage. In large motors, the freewheeling diode or inductor is used to resist the reverse voltage but in small DC motors capacitor is used.

