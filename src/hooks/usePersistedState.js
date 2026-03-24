import { useState, useEffect } from 'react';

function usePersistedState(key, initialValue) {
    const [state, setState] = useState(() => {
        const value = window.localStorage.getItem(key);
        return value !== null ? JSON.parse(value) : initialValue;
    });

    useEffect(() => {
        window.localStorage.setItem(key, JSON.stringify(state));
    }, [key, state]);

    return [state, setState];
}

export default usePersistedState;