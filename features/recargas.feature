Feature: Calculo de recargas de celular
  Como usuario de RecargaYa
  Quiero calcular el valor final de una recarga
  Para conocer la bonificacion que recibo segun el monto y mi tipo de plan

  Scenario: Recarga menor al minimo permitido
    Given un usuario no premium
    When realiza una recarga de 999 pesos
    Then la recarga debe ser rechazada

  Scenario: Recarga valida sin bonificacion
    Given un usuario no premium
    When realiza una recarga de 5000 pesos
    Then el valor final debe ser 5000 pesos
    And la bonificacion debe ser 0 pesos

  Scenario: Recarga con bonificacion del 10 por ciento
    Given un usuario no premium
    When realiza una recarga de 10000 pesos
    Then el valor final debe ser 11000 pesos
    And la bonificacion debe ser 1000 pesos

  Scenario: Recarga con bonificacion del 25 por ciento
    Given un usuario no premium
    When realiza una recarga de 30000 pesos
    Then el valor final debe ser 37500 pesos
    And la bonificacion debe ser 7500 pesos

  Scenario: Usuario premium con bonificacion adicional
    Given un usuario premium
    When realiza una recarga de 10000 pesos
    Then el valor final debe ser 11050 pesos
    And la bonificacion debe ser 1050 pesos

  Scenario Outline: Validacion de montos limite
    Given un usuario no premium
    When realiza una recarga de <monto> pesos
    Then el resultado debe ser "<resultado>"

    Examples:
      | monto | resultado |
      | 999   | rechazado |
      | 1000  | aceptado  |
      | 50000 | aceptado  |
      | 50001 | rechazado |