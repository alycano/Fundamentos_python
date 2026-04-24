# 1. Puntaje total
n1, n2, n3 = 1500, 2400, 3100
total_score = n1 + n2 + n3
print("Puntaje total:", total_score)

# 2. Tiempo total en segundos
h, m, s = 2, 30, 45
total_seconds = (h * 3600) + (m * 60) + s
print("Tiempo total en segundos:", total_seconds)

# 3. Daño total
a1, a2, a3 = 450, 320, 600
total_damage = a1 + a2 + a3
print("Daño total causado:", total_damage)

# 4. Experiencia total
exp1, exp2, exp3 = 100, 250, 500
total_exp = exp1 + exp2 + exp3
print("Experiencia total:", total_exp)

# 5. Porcentaje de vida
v_max, v_actual = 200, 150
percent_life = (v_actual / v_max) * 100
print("Porcentaje de vida:", percent_life, "%")

# 6. Oro total
oro1, oro2, oro3 = 50, 120, 80
total_gold = oro1 + oro2 + oro3
print("Oro total:", total_gold)

# 7. Velocidad promedio
dist, tiempo = 1000, 20
speed = dist / tiempo
print("Velocidad promedio:", speed, "m/s")

# 8. Costo de mejoras
m1, m2, m3 = 1000, 5000, 2500
total_cost = m1 + m2 + m3
print("Costo total mejoras:", total_cost)

# 9. Tiempo restante misión
t_total, t_transcurrido = 600, 450
t_restante = t_total - t_transcurrido
print("Tiempo restante:", t_restante, "segundos")

# 10. Nivel promedio equipo
p1, p2, p3 = 15, 20, 10
avg_level = (p1 + p2 + p3) / 3
print("Nivel promedio:", avg_level)

# 11. Daño crítico
daño_base, crit_mult = 120, 1.5
crit_damage = daño_base * crit_mult
print("Daño crítico:", crit_damage)

# 12. Minutos a Horas y Minutos
total_min = 135
horas = total_min // 60
minutos_restantes = total_min % 60
print("Tiempo:", horas, "horas y", minutos_restantes, "minutos")

# 13. Porcentaje misiones
m_totales, m_listas = 20, 15
pct_misiones = (m_listas / m_totales) * 100
print("Misiones completadas:", pct_misiones, "%")

# 14. Costo tienda
obj1, obj2, obj3 = 15, 30, 100
total_tienda = obj1 + obj2 + obj3
print("Costo total tienda:", total_tienda)

# 15. Tiempo promedio partida
par1, par2, par3 = 10, 15, 12
avg_time = (par1 + par2 + par3) / 3
print("Tiempo promedio de partida:", avg_time)

# 16. Porcentaje enemigos derrotados
e_total, e_derrotados = 50, 42
pct_enemigos = (e_derrotados / e_total) * 100
print("Enemigos derrotados:", pct_enemigos, "%")