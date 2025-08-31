#include <SFML/Graphics.hpp>
#include <iostream>
#include <cmath>

//Notes for self cuz i'm gonna forget especially the SFML stuff
//Creates a class, with attributes

//Also they're all floats instead of double cuz one method needs float and i didn't want to worry about typecasting lol
//Also the dependencies are not in here lol sorry if you try to run this

class PID {
public:
    float kp;
    float ki;
    float kd;

    float prevError;
    float integral;

    //Constructor (Method), Member initialization list (very fast!)
    PID(float kp_, float ki_, float kd_) : kp(kp_), ki(ki_),kd(kd_), prevError(0), integral(0) {}

    //Method
    float correctionForce(float datum, float measured, float dt) {
        float error = measured - datum;
        //Integral gets stored across time, but derivative and error is at that instant. 

        integral += error * dt;

        //Clamp the integral cuz it breaks?
        if (integral > 100) integral = 100;
        if (integral < -100) integral = -100;

        float derivative = (error - prevError) / dt;
        prevError = error;
        //Force has to be opposite of the 
        return -1.0 * (kp * error + ki * integral + kd * derivative);
    }
};

int main()
{
    //Makes da window. (Window dimensions, Title, (optional) style, (optional) window/fullscreen)
    sf::RenderWindow window(sf::VideoMode({ 800, 600 }), "PID", sf::Style::Default, sf::State::Windowed);
    
    //Makes the PID object with kp, ki, kd
    //PID pidObject(.5, 0.01, 0.05);
    PID pidObject(2, 0.1, 1);

    //Initial Pos, vel, etc
    float pos = 400.0;
    float vel = 0.0;
    float datum = 400.0;
    float dt = 0.01;
    float damping = 0.1;
    float mass = 10.0;


    sf::CircleShape ball(20);
    ball.setOrigin({ 20, 20 });
    ball.setFillColor(sf::Color::Red);

    sf::RectangleShape line({ 200.0, 4.0 });
    line.setOrigin({ -200.0, 402.0 });
    line.rotate(sf::degrees(90));
    line.setFillColor(sf::Color::Black);

    sf::Clock clock;

    while (window.isOpen()) {
        while (std::optional event = window.pollEvent()) {
            if (event->is<sf::Event::Closed>()) window.close();

            else if (const auto* keyPressed = event->getIf < sf::Event::KeyPressed >()) {
                if (keyPressed->scancode == sf::Keyboard::Scancode::Space) {
                    //vel += 100;
                    pos += 1000;
                }
                else if (keyPressed->scancode == sf::Keyboard::Scancode::Escape) window.close();
            }
        }

        float crt = pidObject.correctionForce(datum, pos, dt);
        //Maybe add damping again?
        float accel = (crt - damping * vel) / mass;
        vel += accel * dt;
        pos += vel * dt;

        window.clear(sf::Color::White);
        ball.setPosition({ pos, 300.0 });
        window.draw(line);
        window.draw(ball);
        window.display();
    }

    return 0;
}