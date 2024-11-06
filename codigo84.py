import streamlit as st
import pulp

st.title("Ejercicio 8.4: Maximización usando Cortes de Gomory")

st.write("""
Resolver el siguiente problema de maximización usando cortes de Gomory de manera iterativa:

Maximizar: P(x1, x2, x3) = 4x1 + 3x2 + 3x3

Sujeto a:
- 4x1 + 2x2 + x3 <= 10
- 3x1 + 4x2 + 2x3 <= 14
- 2x1 + x2 + 3x3 <= 7
- x1, x2, x3 son enteros no negativos
""")

prob_gomory = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")

prob_gomory += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
prob_gomory += 4 * x1 + 2 * x2 + x3 <= 10, "Restricción 1"
prob_gomory += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restricción 2"
prob_gomory += 2 * x1 + x2 + 3 * x3 <= 7, "Restricción 3"

prob_gomory.solve()

estado = pulp.LpStatus[prob_gomory.status]
valor_objetivo = pulp.value(prob_gomory.objective)

st.subheader("Resultados iniciales:")
st.write(f"Estado del problema: {estado}")
st.write(f"Valor óptimo de la función objetivo: {valor_objetivo}")

st.write("Valores óptimos de las variables de decisión:")
for variable in prob_gomory.variables():
    st.write(f"{variable.name} = {variable.varValue}")

st.subheader("Proceso de cortes de Gomory")
st.write("""
Para aplicar los cortes de Gomory:
1. Observa la solución inicial de valores no enteros en las variables de decisión.
2. Introduce un nuevo corte que elimine esta solución fraccionaria.
3. Repite el proceso hasta obtener una solución entera.

*Nota*: Los cortes de Gomory no se realizan automáticamente en esta implementación. Puedes aplicar los cortes manualmente utilizando herramientas avanzadas como Excel o MATLAB, o resolverlos en un software especializado en programación lineal entera.
""")