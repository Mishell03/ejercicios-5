import streamlit as st
import pulp

st.title("Ejercicio 8.1: Método Branch and Bound")

st.write("""
Resolver el problema de maximización usando el Método Branch and Bound:

Maximizar: P(x1, x2, x3) = 4x1 + 3x2 + 3x3

Sujeto a:
- 4x1 + 2x2 + x3 <= 10
- 3x1 + 4x2 + 2x3 <= 14
- 2x1 + x2 + 3x3 <= 7
- x1, x2, x3 son enteros no negativos
""")

prob = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")

prob += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
prob += 4 * x1 + 2 * x2 + x3 <= 10, "Restricción 1"
prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restricción 2"
prob += 2 * x1 + x2 + 3 * x3 <= 7, "Restricción 3"

prob.solve()

estado = pulp.LpStatus[prob.status]
valor_objetivo = pulp.value(prob.objective)

st.subheader("Resultados:")
st.write(f"Estado del problema: {estado}")
st.write(f"Valor óptimo de la función objetivo: {valor_objetivo}")

st.write("Valores óptimos de las variables de decisión:")
for variable in prob.variables():
    st.write(f"{variable.name} = {variable.varValue}")