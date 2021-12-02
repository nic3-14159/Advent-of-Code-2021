SELECT
(SELECT SUM(X) FROM Input WHERE Command="forward")*
((SELECT SUM(X) FROM Input WHERE Command="down")-
(SELECT SUM(X) FROM Input WHERE Command="up"))
AS Part1,
SUM(depth)*(SELECT SUM(X) FROM Input WHERE Command="forward") AS part2
FROM
(
	SELECT rownum, A.Command, (SUM(aim_down) OVER (ORDER BY rownum) - SUM(aim_up) OVER (ORDER BY rownum)) * B.X as depth
	FROM
	(
		(
			SELECT ROWID AS rownum, Command, 0 as aim_up
			FROM Input
			WHERE NOT Command = "up"
			UNION
			SELECT ROWID AS rownum, Command, X as aim_up
			FROM Input
			WHERE Command="up"
		)
		NATURAL JOIN
		(
			SELECT ROWID AS rownum, Command, 0 as aim_down
			FROM Input
			WHERE NOT Command = "down"
			UNION
			SELECT ROWID AS rownum, Command, X as aim_down
			FROM Input
			WHERE Command="down"
		)
	) A, Input B
	WHERE B.ROWID = rownum
)
WHERE Command = "forward"