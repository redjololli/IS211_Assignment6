#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Week 6 Assignment Convensions Refactored


class ConversionNotPossible(Exception): 
    pass

def convert(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return value
    if fromUnit in ('cel', 'fah', 'kel'):
        if fromUnit == 'cel' and toUnit ==  'kel':
            return convertCelsiusToKelvin(value)
        if fromUnit == 'cel' and toUnit ==  'fah':
            return convertCelsiusToFahrenheit(value)
        if fromUnit == 'kel' and toUnit ==  'cel':
            return convertKelvinToCelsius(value)
        if fromUnit == 'kel' and toUnit ==  'fah':
            return convertKelvinToFahrenheit(value)  
        if fromUnit == 'fah' and toUnit ==  'cel':
            return convertFahrenheitToCelsius(value) 
        if fromUnit == 'fah' and toUnit ==  'kel':
            return convertFahrenheitToKelvin(value)
        
    if fromUnit in ('met', 'mil', 'yar'):
        if fromUnit == 'met' and toUnit ==  'mil':
            return convertMetersToMiles(value)
        if fromUnit == 'met' and toUnit ==  'yar':
            return convertMetersToYards(value)
        if fromUnit == 'mil' and toUnit ==  'met':
            return convertMilesToMeters(value)
        if fromUnit == 'mil' and toUnit ==  'yar':
            return convertMilesToYards(value)  
        if fromUnit == 'yar' and toUnit ==  'met':
            return convertYardsToMeters(value) 
        if fromUnit == 'yar' and toUnit ==  'mil':
            return convertYardsToMiles(value)
    else:
        raise ConversionNotPossible("Conversion not possible")


def convertCelsiusToKelvin(cel):
    cel = float(cel)
    kel = cel + 273.15
    return round(kel, 2)

def convertCelsiusToFahrenheit(cel):
    cel = float(cel)
    fah = cel * 1.8 + 32
    return round(fah, 2)

def convertFahrenheitToCelsius(fah):
     fah = float(fah)
     cel = (fah - 32) * 0.5555555555555556
     return round(cel, 2)

def convertFahrenheitToKelvin(fah):
     fah = float(fah)
     kel = (fah + 459.67) * 0.5555555555555556
     return round(kel,2)   

def convertKelvinToCelsius(kel):
    kel = float(kel)
    cel = round(kel - 273.15, 2)
    return cel

def convertKelvinToFahrenheit(kel):
    kel = float(kel)
    fah = round(kel * 1.8 - 459.67, 2)
    return fah

def convertMilesToYards(mil):
    mil = float(mil)
    yar = mil * 1760
    return round(yar, 2)

def convertMilesToMeters(mil):
    mil = float(mil)
    mer = mil * 1609.344
    return round(mer, 2)

def convertYardsToMiles(yar):
    yar = float(yar)
    mil = yar / 1760
    return round(mil, 2)
    
def convertYardsToMeters(yar):
    yar = float(yar)
    met = yar / 1.0936
    return round(met, 2)

def convertMetersToMiles(met):
    met = float(met)
    mil = met / 1609.344
    return round(mil, 2)

def convertMetersToYards(met):
    met = float(met)
    yar = met * 1.0936
    return round(yar, 2)


# In[5]:


convert('cel', 'kel', 300.00)

