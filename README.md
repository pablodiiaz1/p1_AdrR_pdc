# Practica 1 Ampliación de Robótica

## Explicación para poder ejecutar los ejercicios:

Para ejecutar el publisher-subscriber, solo hay que hacer:

	ros2 run p1_adr_rme navsatfixpublisher
	ros2 run p1_adr_rme navsatfixsubscriber
  
Para ejecutar el service client: 

	ros2 run p1_adr_rme squareservice
	ros2 run p1_adr_rme squareclient a b
 
siendo *a* el número al que vamos a calcular el cuadrado y *b* un número cualquiera, ya que no lo utilizaremos para nada.
