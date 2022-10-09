s = 'abaabbbbba'
ans = '' #самая частая буква
anscnt = 0 #сколько раз она встречалась
for i in range(len(s)):
	nowcnt = 0 #(текущее)берем первую внешнюю букву и начинаем считать, перебирая все буквы
	for j in range(len(s)):
		if s[i] == s[j]:
			nowcnt +=1
	if nowcnt > anscnt:
		ans = s[i]
		anscnt = nowcnt
print(ans)
print(anscnt)
