import streamlit as st
import pulp

st.title("Ejercicio 8.3: Minimización usando Cortes de Gomory")

st.write("""
Resolver el siguiente problema de minimización usando cortes de Gomory de manera iterativa:

Minimizar: C(x, y) = x - y

Sujeto a:
- 3x + 4y <= 6
- x - y <= 1
- x, y son enteros no negativos
""")

prob_gomory = pulp.LpProblem("Minimizar_C", pulp.LpMinimize)

x = pulp.LpVariable("x", lowBound=0, cat="Integer")
y = pulp.LpVariable("y", lowBound=0, cat="Integer")

prob_gomory += x - y, "Función Objetivo"
prob_gomory += 3 * x + 4 * y <= 6, "Restricción 1"
prob_gomory += x - y <= 1, "Restricción 2"

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