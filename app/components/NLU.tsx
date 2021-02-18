import React, {FunctionComponent, useState} from 'react';
import {
  StyleSheet,
  TextInput,
  Button,
  View,
  Text,
  StatusBar,
  ActivityIndicator,
} from 'react-native';

import {getPredictionFromApiWithSearchedText} from '../api/nlu_api';

const NLU: FunctionComponent<{}> = () => {
  const placeholder = 'Is it sunny in Paris, France right now?';
  const [input, setInput] = useState<string>('');
  const [prediction, setPrediction] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const _displayLoading = () => {
    if (isLoading) {
      return (
        <View style={styles.loading_container}>
          <ActivityIndicator size="large" />
        </View>
      );
    }
  };

  const _runService = () => {
    if (input.length>0) {
    setIsLoading(true);
    getPredictionFromApiWithSearchedText(input).then((data) => {
      if (data.statusCode == '200') {
        setPrediction(data.result);
        setIsLoading(false);
      }
    });
  };
  };

  return (
    <View>
      <StatusBar barStyle="dark-content" />
      <View style={styles.search_container}>
        <TextInput
          placeholder={placeholder}
          style={styles.text_input}
          onChangeText={(input) => {
            setInput(input);
            if (input.length == 0){
              setPrediction("")
            }
          }}
          onSubmitEditing={() => _runService()}
        />
        <View style={styles.button}>
        <Button
          color={styles.button.color}
          onPress={() => _runService()}
          title="Submit"
        />
        </View>
        {_displayLoading()}
        <Text style={styles.text_field}>Input</Text>
        <Text style={styles.text_prediction}>{input}</Text>
        <Text style={styles.text_field}>Prediction</Text>
        <Text style={styles.text_prediction}>{prediction}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  header: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  text_header: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 30,
    marginBottom: 10,
    marginTop: 100,
  },
  text_description: {
    color: 'white',
    fontSize: 20,
  },
  search_container: {
    flex: 1,
    marginTop: 0,
    alignItems: 'center',
  },
  text_input: {
    padding: 10,
    fontSize: 12,
    height: 50,
    width: 400,
    marginLeft: 5,
    marginRight: 5,
    borderColor: '#000000',
    borderRadius: 25,
    borderWidth: 1,
    paddingLeft: 5,
    backgroundColor: 'white',
  },
  text_field: {
    color: "#61dafb",
    marginTop: 50,
    fontSize: 20,
    fontWeight: 'bold',
  },
  text_prediction: {
    color: 'white',
    marginTop: 20,
    fontSize: 15,
  },
  button:{
    color: "#61dafb",
    marginBottom: 50,
  }
});

export default NLU;
