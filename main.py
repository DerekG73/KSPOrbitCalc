# import numpy as np
import math


class OrbitalEquations():
  def __init__(self):
    self.gravConstant = 6.6743e-11
    self.kerbinMass = 5.2916e22
    self.kerbinRadius = 6e5

  def hohmannTransferdV(self,planetName,alt1,alt2) -> float:
    match planetName:
      case "kerbin":
        mu = self.gravConstant*self.kerbinMass
        r1 = alt1 + self.kerbinRadius
        r2 = alt2 + self.kerbinRadius
      case _:
        print("Invalid entry")

    #Vis Viva equation
    circularOrbitV1 = (mu/r1)**0.5
    dV1 = circularOrbitV1*((2*r2/(r1 + r2))**0.5 - 1)
    #circularize:
    circularOrbitV2 = (mu/r2)**0.5
    dV2 = circularOrbitV2*((2*r1/(r1 + r2))**0.5 - 1)

    return [dV1,dV2]

  def escapedV(self,planetName,initMass,finalMass,specImpulse):
    match planetName:
        case "kerbin":
          mu = self.gravConstant*self.kerbinMass
        case _:
          print("Invalid entry")
    g = mu/(self.kerbinRadius**2)
    dV = specImpulse * g * math.log(initMass/finalMass)

    return dV

def main():
  OE = OrbitalEquations()
  planet = "kerbin"
  altitude1 = 80e3
  altitude2 = 300e3
  [burn1, burn2] = OE.hohmannTransferdV(planet,altitude1,altitude2)
  print(f"first burn: {burn1:.2f}, second burn: {burn2:.2f}")

  initialMass = 11.7
  finalMass = 5.6
  impulse = 175
  escapeDeltaV = OE.escapedV(planet,initialMass,finalMass,impulse)
  print(f"escape delta V: {escapeDeltaV:.2f}")

if __name__ == "__main__":
  main()
