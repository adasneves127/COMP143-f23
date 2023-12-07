#include <stdio.h> 

float fahrenheitToCelcius(float fahrenheit){
    return (fahrenheit - 32) * 5.0/9.0;
}


float celciusToFahrenheit(float celcius){
    return (celcius * 9.0/5.0) + 32;
}

int main(void){
    float zeroC = 212.0;
    float convC = fahrenheitToCelcius(zeroC);
    printf("%f", convC);
}