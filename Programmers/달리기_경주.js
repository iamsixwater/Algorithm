function solution(players, callings) {
    let name = {};
    let rank = {};
    for(let i = 0; i < players.length; i++) {
        name[players[i]] = i;
        rank[Number(i)] = players[i];
    }

    for(let i = 0; i < callings.length; i++) {
        let passing_name = callings[i]; // kai
        let passing_rank = name[passing_name]; // 3
        let origin_rank = passing_rank - 1; // 2
        let origin_name = rank[origin_rank]; // poe

        name[passing_name] = origin_rank;
        name[origin_name] = passing_rank;

        rank[passing_rank] = origin_name;
        rank[origin_rank] = passing_name;
    }

    let answer = [];
    for(let key in rank) {
        answer.push(rank[key]);
    }

    return answer;
}
