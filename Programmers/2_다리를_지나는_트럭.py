def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    seconds = 0
    sum_weight = 0
    
    while bridge:
        seconds += 1
        sum_weight -= bridge.pop(0)
        
        if truck_weights:
            if sum_weight + truck_weights[0] <= weight:
                sum_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    
    return seconds